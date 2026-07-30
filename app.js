/* 正心童学·初中数学知识点汇总 — app.js
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

  marked.setOptions({ breaks: true, gfm: true });

  function getBasePath() {
    var path = window.location.pathname;
    if (path.indexOf('zhengxin-math-prep') !== -1) {
      var idx = path.indexOf('zhengxin-math-prep');
      return path.substring(0, idx + 'zhengxin-math-prep'.length) + '/';
    }
    return './';
  }

  var BASE = getBasePath();

  function parseFrontmatter(text) {
    var fm = {};
    var match = text.match(/^---\s*\n([\s\S]*?)\n---\s*\n([\s\S]*)$/);
    if (!match) return { frontmatter: fm, body: text };
    var lines = match[1].split('\n');
    lines.forEach(function (line) {
      var idx = line.indexOf(':');
      if (idx > 0) {
        fm[line.slice(0, idx).trim()] = line.slice(idx + 1).trim();
      }
    });
    return { frontmatter: fm, body: match[2] };
  }

  function renderWikiLinks(html) {
    return html.replace(/\[\[([^\]]+)\]\]/g, function (match, link) {
      var text = link.trim();
      var href = BASE + text + '.md';
      var safeHref = href.replace(/'/g, "\\'");
      return '<a class="wiki-link" href="' + href + '" data-wiki="' + safeHref + '">' + text + '</a>';
    });
  }

  function setupModuleSections(container) {
    container.querySelectorAll('h2').forEach(function (h2) {
      var text = h2.textContent;
      if (text.indexOf('📖') !== -1 || text.indexOf('知识点') !== -1) {
        h2.classList.add('section-knowledge');
      } else if (text.indexOf('⭐') !== -1 || text.indexOf('重点') !== -1) {
        h2.classList.add('section-key');
      } else if (text.indexOf('⚠️') !== -1 || text.indexOf('易错') !== -1) {
        h2.classList.add('section-warn');
      } else if (text.indexOf('📝') !== -1 || text.indexOf('例题') !== -1) {
        h2.classList.add('section-example');
      }
    });
  }

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
      var sidebarOpen = ref(false);
      var chaptersStatus = ref('');

      var metaLabels = {
        grade: '年级',
        unit: '章节',
        knowledge: '知识点',
        source: '出处',
        difficulty: '难度',
        status: '状态',
        date: '日期'
      };

      var filteredGrades = computed(function () {
        var q = searchQuery.value.trim().toLowerCase();
        var grades = config.value.grades || {};
        if (!q) {
          var result = {};
          Object.keys(grades).forEach(function (key) { result[key] = grades[key]; });
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

      function toggleSidebar() {
        sidebarOpen.value = !sidebarOpen.value;
      }

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
        sidebarOpen.value = false;
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

          var html = marked.parse(parsed.body);
          html = renderWikiLinks(html);
          renderedHtml.value = html;

          await nextTick();
          var container = document.querySelector('.markdown-body');
          if (container) {
            setupModuleSections(container);
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

      watch(searchQuery, function (q) {
        if (q.trim()) {
          Object.keys(config.value.grades || {}).forEach(function (key) {
            if (expandedGrades.value.indexOf(key) === -1) {
              expandedGrades.value.push(key);
            }
          });
        }
      });

      onMounted(async function () {
        try {
          var saved = localStorage.getItem('zx-theme');
          if (saved === 'dark') {
            isDark.value = true;
            document.documentElement.setAttribute('data-theme', 'dark');
          }
        } catch (e) {}

        try {
          var resp = await fetch(BASE + 'config.json?t=' + Date.now());
          if (!resp.ok) throw new Error('config.json 加载失败 (' + resp.status + ')');
          config.value = await resp.json();
          chaptersStatus.value = config.value.chapters_status || '';
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
        sidebarOpen: sidebarOpen,
        chaptersStatus: chaptersStatus,
        metaLabels: metaLabels,
        metaDisplay: metaDisplay,
        filteredGrades: filteredGrades,
        toggleGrade: toggleGrade,
        toggleChapter: toggleChapter,
        goGrade: goGrade,
        toggleTheme: toggleTheme,
        toggleSidebar: toggleSidebar,
        loadLesson: loadLesson,
        retryLoad: retryLoad
      };
    }
  });

  app.mount('#app');
})();