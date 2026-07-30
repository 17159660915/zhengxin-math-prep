/* 正心童学·初中数学备课系统 — app.js
 * Vue3 + marked + KaTeX 单页应用
 * 无构建步骤，纯 CDN
 */

(function () {
  'use strict';

  var createApp = Vue.createApp;
  var ref = Vue.ref;
  var computed = Vue.computed;
  var watch = Vue.watch;
  var onMounted = Vue.onMounted;
  var nextTick = Vue.nextTick;

  // ---- marked 配置 ----
  marked.setOptions({
    breaks: true,
    gfm: true
  });

  // ---- 基础路径检测（本地 vs GitHub Pages）----
  function getBasePath() {
    var path = window.location.pathname;
    // GitHub Pages: /zhengxin-math-prep/
    if (path.indexOf('zhengxin-math-prep') !== -1) {
      var idx = path.indexOf('zhengxin-math-prep');
      return path.substring(0, idx + 'zhengxin-math-prep'.length) + '/';
    }
    return './';
  }

  var BASE = getBasePath();

  // ---- frontmatter 解析（轻量正则，不引大库）----
  function parseFrontmatter(text) {
    var fm = {};
    var match = text.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/);
    if (!match) return { frontmatter: fm, body: text };
    var lines = match[1].split('\n');
    lines.forEach(function (line) {
      var idx = line.indexOf(':');
      if (idx > 0) {
        var key = line.slice(0, idx).trim();
        var val = line.slice(idx + 1).trim();
        fm[key] = val;
      }
    });
    return { frontmatter: fm, body: match[2] };
  }

  // ---- [[双链]] 渲染为可点击链接 ----
  function renderWikiLinks(html) {
    return html.replace(/\[\[([^\]]+)\]\]/g, function (match, link) {
      var text = link.trim();
      var href = '#';
      // 映射到教法骨架文件
      if (text.indexOf('四步教学法') !== -1 || text.indexOf('自主学习') !== -1) {
        href = BASE + '_教法骨架/自主学习四步教学法.md';
      } else if (text.indexOf('降维打击') !== -1) {
        href = BASE + '_教法骨架/降维打击策略.md';
      } else if (text.indexOf('游戏化') !== -1) {
        href = BASE + '_教法骨架/游戏化教学设计.md';
      } else if (text.indexOf('评估') !== -1) {
        href = BASE + '_教法骨架/学生评估标准.md';
      } else {
        href = BASE + text + '.md';
      }
      var safeHref = href.replace(/'/g, "\\'");
      return '<a class="wiki-link" href="' + href + '" data-wiki="' + safeHref + '">' + text + '</a>';
    });
  }

  // ---- KaTeX 自动渲染 ----
  function renderMath(container) {
    if (typeof renderMathInElement === 'function') {
      renderMathInElement(container, {
        delimiters: [
          { left: '$$', right: '$$', display: true },
          { left: '$', right: '$', display: false },
          { left: '\\(', right: '\\)', display: false },
          { left: '\\[', right: '\\]', display: true }
        ],
        throwOnError: false
      });
    }
  }

  // ---- 折叠来源引用块 ----
  function setupCollapsibleQuotes(container) {
    var blockquotes = container.querySelectorAll('blockquote');
    blockquotes.forEach(function (bq) {
      var text = bq.textContent.trim();
      if (text.indexOf('来源') === 0 || text.indexOf('原文摘录') !== -1) {
        var wrapper = document.createElement('div');
        wrapper.className = 'collapsible-quote';
        var header = document.createElement('div');
        header.className = 'collapsible-header';
        header.innerHTML = '📄 ' + text.split('\n')[0].slice(0, 50) + '… <span class="toggle-hint">点击展开</span>';
        var body = document.createElement('div');
        body.className = 'collapsible-body';
        body.style.display = 'none';
        bq.parentNode.insertBefore(wrapper, bq);
        body.appendChild(bq);
        wrapper.appendChild(header);
        wrapper.appendChild(body);
        header.addEventListener('click', function () {
          if (body.style.display === 'none') {
            body.style.display = 'block';
            header.querySelector('.toggle-hint').textContent = '点击收起';
            wrapper.classList.add('open');
          } else {
            body.style.display = 'none';
            header.querySelector('.toggle-hint').textContent = '点击展开';
            wrapper.classList.remove('open');
          }
        });
      }
    });
  }

  // ---- Vue App ----
  var app = createApp({
    setup: function () {
      var config = ref({ site: {}, grades: {} });
      var currentPath = ref('');
      var currentLesson = ref(null);
      var renderedHtml = ref('');
      var loading = ref(false);
      var error = ref('');
      var searchQuery = ref('');
      var expandedGrades = ref([]);
      var expandedChapters = ref([]);
      var isDark = ref(false);
      var showMethods = ref(false);
      var chaptersStatus = ref('');

      var metaLabels = {
        grade: '年级',
        unit: '单元',
        knowledge: '知识点',
        source: '出处',
        difficulty: '难度',
        status: '状态',
        date: '日期',
        type: '类型',
        last_sync: '同步日期',
        source_date: '来源日期'
      };

      var methodFiles = [
        { title: '自主学习四步教学法', file: '_教法骨架/自主学习四步教学法.md' },
        { title: '降维打击策略', file: '_教法骨架/降维打击策略.md' },
        { title: '游戏化教学设计', file: '_教法骨架/游戏化教学设计.md' },
        { title: '学生评估标准', file: '_教法骨架/学生评估标准.md' }
      ];

      // ---- 计算属性：过滤后的年级（搜索功能）----
      var filteredGrades = computed(function () {
        var q = searchQuery.value.trim().toLowerCase();
        var grades = config.value.grades || {};
        if (!q) {
          var result = {};
          Object.keys(grades).forEach(function (key) {
            result[key] = grades[key];
          });
          return result;
        }
        var filtered = {};
        Object.keys(grades).forEach(function (key) {
          var grade = grades[key];
          if (grade.label.toLowerCase().indexOf(q) !== -1) {
            filtered[key] = grade;
            return;
          }
          var chapters = (grade.chapters || []).map(function (ch) {
            var topics = (ch.topics || []).filter(function (t) {
              return t.title.toLowerCase().indexOf(q) !== -1 ||
                     t.id.toLowerCase().indexOf(q) !== -1;
            });
            return Object.assign({}, ch, { topics: topics });
          }).filter(function (ch) {
            return ch.topics.length > 0 || ch.title.toLowerCase().indexOf(q) !== -1;
          });
          if (chapters.length > 0) {
            filtered[key] = Object.assign({}, grade, { chapters: chapters });
          }
        });
        return filtered;
      });

      // ---- 计算属性：元信息展示 ----
      var metaDisplay = computed(function () {
        if (!currentLesson.value || !currentLesson.value.frontmatter) return {};
        var fm = currentLesson.value.frontmatter;
        var out = {};
        Object.keys(metaLabels).forEach(function (k) {
          if (fm[k] !== undefined && fm[k] !== '') {
            out[k] = fm[k];
          }
        });
        return out;
      });

      // ---- 方法 ----
      function toggleGrade(key) {
        var idx = expandedGrades.value.indexOf(key);
        if (idx === -1) expandedGrades.value.push(key);
        else expandedGrades.value.splice(idx, 1);
      }

      function toggleChapter(id) {
        var idx = expandedChapters.value.indexOf(id);
        if (idx === -1) expandedChapters.value.push(id);
        else expandedChapters.value.splice(idx, 1);
      }

      function goGrade(key) {
        if (expandedGrades.value.indexOf(key) === -1) {
          expandedGrades.value.push(key);
        }
      }

      function goMethod() {
        showMethods.value = true;
      }

      function statusLabel(status) {
        var map = {
          '已备课': '✅',
          '待备课': '📝',
          '待核实': '⚠️',
          '样板教案': '⭐'
        };
        return map[status] || '';
      }

      function toggleTheme() {
        isDark.value = !isDark.value;
        if (isDark.value) {
          document.documentElement.setAttribute('data-theme', 'dark');
        } else {
          document.documentElement.setAttribute('data-theme', 'light');
        }
        try { localStorage.setItem('zx-theme', isDark.value ? 'dark' : 'light'); } catch (e) {}
      }

      async function loadLesson(filePath) {
        if (!filePath) return;
        currentPath.value = filePath;
        loading.value = true;
        error.value = '';
        currentLesson.value = null;
        renderedHtml.value = '';

        try {
          var url = BASE + filePath + '?t=' + Date.now();
          var resp = await fetch(url);
          if (!resp.ok) throw new Error('文件加载失败 (' + resp.status + ')：' + filePath);
          var text = await resp.text();
          var parsed = parseFrontmatter(text);
          currentLesson.value = { frontmatter: parsed.frontmatter };

          // 渲染 Markdown → 双链替换 → 写入 DOM
          var html = marked.parse(parsed.body);
          html = renderWikiLinks(html);
          renderedHtml.value = html;

          // 等 DOM 更新后渲染 KaTeX 和折叠引用
          await nextTick();
          var container = document.querySelector('.markdown-body');
          if (container) {
            renderMath(container);
            setupCollapsibleQuotes(container);
            // 绑定 wiki 链接点击
            var wikiLinks = container.querySelectorAll('.wiki-link');
            wikiLinks.forEach(function (link) {
              link.addEventListener('click', function (e) {
                e.preventDefault();
                var href = link.getAttribute('data-wiki');
                if (href && href !== '#') {
                  var relPath = href.replace(BASE, '');
                  loadLesson(relPath);
                }
              });
            });
          }
        } catch (err) {
          error.value = err.message;
        } finally {
          loading.value = false;
        }
      }

      function retryLoad() {
        if (currentPath.value) {
          loadLesson(currentPath.value);
        }
      }

      // ---- 搜索监听：自动展开匹配项 ----
      watch(searchQuery, function (q) {
        if (q.trim()) {
          // 搜索时自动展开所有年级
          Object.keys(config.value.grades || {}).forEach(function (key) {
            if (expandedGrades.value.indexOf(key) === -1) {
              expandedGrades.value.push(key);
            }
          });
        }
      });

      // ---- 初始化 ----
      onMounted(async function () {
        // 读取主题偏好
        try {
          var saved = localStorage.getItem('zx-theme');
          if (saved === 'dark') {
            isDark.value = true;
            document.documentElement.setAttribute('data-theme', 'dark');
          }
        } catch (e) {}

        // 加载 config.json
        try {
          var resp = await fetch(BASE + 'config.json?t=' + Date.now());
          if (!resp.ok) throw new Error('config.json 加载失败 (' + resp.status + ')');
          config.value = await resp.json();
          chaptersStatus.value = config.value.chapters_status || '';
          // 默认展开第一个年级
          var keys = Object.keys(config.value.grades || {});
          if (keys.length > 0) {
            expandedGrades.value = [keys[0]];
          }
        } catch (err) {
          error.value = '加载配置失败：' + err.message;
        }
      });

      return {
        config: config,
        currentPath: currentPath,
        currentLesson: currentLesson,
        renderedHtml: renderedHtml,
        loading: loading,
        error: error,
        searchQuery: searchQuery,
        expandedGrades: expandedGrades,
        expandedChapters: expandedChapters,
        isDark: isDark,
        showMethods: showMethods,
        chaptersStatus: chaptersStatus,
        metaLabels: metaLabels,
        metaDisplay: metaDisplay,
        methodFiles: methodFiles,
        filteredGrades: filteredGrades,
        toggleGrade: toggleGrade,
        toggleChapter: toggleChapter,
        goGrade: goGrade,
        goMethod: goMethod,
        statusLabel: statusLabel,
        toggleTheme: toggleTheme,
        loadLesson: loadLesson,
        retryLoad: retryLoad
      };
    }
  });

  app.mount('#app');
})();
