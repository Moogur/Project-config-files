﻿import os
import shutil
import json

directory = {
    'sass': ('grid', 'core', 'layout'),
    'js': ('functions', ),
    'img': bool,
    'fonts': bool,
    'pug': bool
}
file_sass = {
  'core': ('_fonts.sass', '_base.sass', '_variables.sass'),
  'grid': ('_smart-grid-percentage.sass', '_smart-grid-rem.sass', '_smart-grid.sass', '_grid.sass')
}
symlink_node_modules = r'/Users/dilkree/IT/JS_MODULES/node_modules'
get_directory = os.getcwd()


def dev_primary_progect():
    # TODO создание дерева папок для проекта
    for i in directory:
        if type(directory[i]) is tuple:
            for j in directory[i]:
                os.makedirs(fr'{get_directory}/app/{i}/{j}')
        else:
            os.mkdir(fr'{get_directory}/app/{i}')
    # TODO создание символической ссылки на node_modules
    os.symlink(symlink_node_modules, 'node_modules')
    print('---------------------------------------')
    print('Дерево каталогов проекта успешно создано')
    # TODO создание файла package.json
    if not os.path.isfile(os.path.join(get_directory, 'package.json')):
        os.system('npm init -y')
    print('---------------------------------------')
    print('Файл package.json успешно создан')
    # TODO создание файла .eslintrc
    with open(os.path.join(get_directory, '.eslintrc'), 'w', encoding='utf8') as eslint_file:
        eslint_file.write('''{
"extends": "eslint:recommended",
"parser": "babel-eslint",
"globals": {
    "window": true,
    "document": true,
    "console": true
},
"rules": {
    "no-console": "off"
}
}''')
    # TODO создание файла .babelrc
    with open(fr'{get_directory}/.babelrc', 'w', encoding='utf8') as babel_file:
        babel_file.write('''{
"presets": [
    "@babel/preset-env",
]
}''')
    # TODO создание файла .pug-lintrc
    with open(fr'{get_directory}/.pug-lintrc', 'w', encoding='utf8') as puglint_file:
        puglint_file.write('''{
"disallowAttributeConcatenation": null, "disallowAttributeInterpolation": true,
"disallowBlockExpansion": null, "disallowClassAttributeWithStaticValue": true, "disallowClassLiterals": null, "disallowClassLiteralsBeforeAttributes": null, "disallowClassLiteralsBeforeIdLiterals": null, "disallowDuplicateAttributes": true,
"disallowHtmlText": null,
"disallowIdAttributeWithStaticValue": null,
"disallowIdLiterals": true,
"disallowIdLiteralsBeforeAttributes": null, "disallowMultipleLineBreaks": true, "disallowSpaceAfterCodeOperator": null, "disallowSpacesInsideAttributeBrackets": true, "disallowSpecificAttributes": [ { "a": "name" } ], "disallowSpecificTags": null,
"disallowStringConcatenation": true, "disallowStringInterpolation": null,
"disallowTagInterpolation": null,
"maximumNumberOfLines": null, "requireClassLiteralsBeforeAttributes": true, "requireClassLiteralsBeforeIdLiterals": true, "requireIdLiteralsBeforeAttributes": true, "requireLineFeedAtFileEnd": true,
"requireLowerCaseAttributes": true,
"requireLowerCaseTags": true,
"requireSpaceAfterCodeOperator": true, "requireSpacesInsideAttributeBrackets": null, "requireSpecificAttributes":
  [
    { "form": "action" },
  	{ "img": "alt" },
	{ "input": "type" },
    { "input[type=submit]": "value" }
  ],
"requireStrictEqualityOperators": true,
"validateAttributeSeparator":
  {
    "separator": ", ",
    "multiLineSeparator": " "
  },
"validateDivTags": true,
"validateExtensions": true,
"validateIndentation": 2,
"validateLineBreaks": "LF",
"validateSelfClosingTags": true
}''')
    # TODO создание файла .sass-lint.yml
    with open(fr'{get_directory}/.sass-lint.yml', 'w', encoding='utf8') as sass_file:
        sass_file.write('''files:
  include: '**/*.sass'
options:
  formatter: stylish
  merge-default-rules: false
rules:
  bem-depth:
    - 0
    - max-depth: 1
  border-zero:
    - 1
    - convention: zero
  brace-style:
    - 1
    - allow-single-line: true
  class-name-format:
    - 1
    - convention: hyphenatedlowercase
  clean-import-paths:
    - 1
    - filename-extension: true
      leading-underscore: true
  empty-line-between-blocks:
    - 1
    - include: true
    - ignore-single-line-rulesets: true
  extends-before-declarations: 1
  extends-before-mixins: 1
  final-newline:
    - 1
    - include: true
  force-attribute-nesting: 1
  force-element-nesting: 1
  force-pseudo-nesting: 0
  function-name-format:
    - 1
    - allow-leading-underscore: true
      convention: hyphenatedlowercase
  hex-length:
    - 1
    - style: long
  hex-notation:
    - 1
    - style: lowercase
  id-name-format:
    - 1
    - convention: hyphenatedlowercase
  indentation:
    - 1
    - size: 2
  leading-zero:
    - 1
    - include: false
  mixin-name-format:
    - 1
    - allow-leading-underscore: true
      convention: hyphenatedlowercase
  mixins-before-declarations: 1
  nesting-depth:
    - 1
    - max-depth: 3
  no-color-keywords: 1
  no-color-literals: 0
  no-css-comments: 1
  no-debug: 1
  no-duplicate-properties: 1
  no-empty-rulesets: 1
  no-extends: 0
  no-ids: 0
  no-important: 1
  no-invalid-hex: 1
  no-mergeable-selectors: 1
  no-misspelled-properties:
    - 1
    - extra-properties: []
  no-qualifying-elements:
    - 1
    - allow-element-with-attribute: false
      allow-element-with-class: false
      allow-element-with-id: false
  no-trailing-zero: 1
  no-transition-all: 0
  no-url-protocols: 1
  no-vendor-prefixes:
    - 1
    - additional-identifiers: []
      excluded-identifiers: []
  placeholder-in-extend: 1
  placeholder-name-format:
    - 1
    - convention: hyphenatedlowercase
  property-sort-order:
    - 0
    - ignore-custom-properties: false
  property-units:
    - 1
    - global:
        - ch
        - em
        - ex
        - rem
        - cm
        - in
        - mm
        - pc
        - pt
        - px
        - q
        - vh
        - vw
        - vmin
        - vmax
        - deg
        - grad
        - rad
        - turn
        - ms
        - s
        - Hz
        - kHz
        - dpi
        - dpcm
        - dppx
        - '%'
      per-property: {}
  quotes:
    - 1
    - style: single
  shorthand-values:
    - 1
    - allowed-shorthands:
        - 1
        - 2
        - 3
  single-line-per-selector: 1
  space-after-bang:
    - 1
    - include: false
  space-after-colon:
    - 1
    - include: true
  space-after-comma:
    - 1
    - include: true
  space-before-bang:
    - 1
    - include: true
  space-before-brace:
    - 1
    - include: true
  space-before-colon: 1
  space-between-parens:
    - 1
    - include: false
  trailing-semicolon: 1
  url-quotes: 1
  variable-for-property:
    - 0
    - properties: []
  variable-name-format:
    - 1
    - allow-leading-underscore: true
      convention: hyphenatedlowercase
  zero-unit: 1''')
# TODO создание файла smart-grid-config.js
    with open(fr'{get_directory}/smart-grid-config.js', 'w', encoding='utf-8') as sg_file:
        sg_file.write(''''use strict';

const smartgrid = require('smart-grid');

// Базовый размер шрифта
const baseFontPx = '16px'; 

const settings = {
  filename: '_smart-grid',
  outputStyle: 'sass', 
  columns: 12,
  offset: '20px', // Расстояние между столбцами (gutter)
  // false => max-width, true => min-width
  mobileFirst: false,  
  container: {
    maxWidth: '1200px', // Ширина макета
    fields: '30px' // Оступы по краям сайта (padding)
  },
  breakPoints: {
    // Bootstrap breakpoint
    xl: {
      width: '1200px',
      fields: "30px"
    },
    lg: {
      width: '992px',
      fields: "16px" 
    },
    md: {
      width: '768px',
      fields: "24px"
    },
    sm: {
      width: '576px',
      fields: '18px' 
    }
  },
  mixinNames: {
    container: "container",
    shift: "offset",
  }, 
  tab: "  "
};

const arr = [undefined, {
  filename: settings.filename + '-percentage',
  offset: (parseInt(settings.offset) / parseInt(settings.container.maxWidth) * 100) + '%'
}, {
  filename: settings.filename + '-rem',
  offset: (parseInt(settings.offset) / parseInt(baseFontPx)) + 'rem'
}];

for (let value of arr) {
  smartgrid('./app/sass/grid', Object.assign(settings, value));
}
''')
    with open(fr'{get_directory}/.gitignore', 'w', encoding='utf8') as git_file:
        git_file.write('''.DS_Store
/dist/
/gulp/
/webpack/
/node_modules
/.gitignore
/.eslintrc
/.babelrc
/.pug-lintrc
/.sass-lint.yml
/package.json
/web.py
/gulpfile.js 
/webpack.config.js
/smart-grid-config.js
**/*.psd
**/maket*.jpg
*.txt''')
    print('---------------------------------------')
    print('Файлы: .babelrc, .eslintrc, .pug-lintrc, .sass-lint.yml, .gitignore, smart-grid-config.js успешно созданы')
    # TODO создание файлов *.sass
    for i in file_sass:
        for j in file_sass[i]:
            with open(fr'{get_directory}/app/sass/{i}/{j}', 'w', encoding='utf8') as sass_file:
                    if j == '_grid.sass':
                        sass_file.write('''+reset()

.debug
  +debug(rgba(0, 0, 0, 0.2), 1px solid #ffff00)

.container
  +container()
''')
                    else:
                        pass
    with open(fr'{get_directory}/app/sass/style.sass', 'w', encoding='utf8') as sass_file:
        sass_file.write('''// Folder: Grid
@import "./grid/_smart-grid.sass"
//@import "./grid/_smart-grid-percentage.sass"
//@import "./grid/_smart-grid-rem.sass"
@import "./grid/_grid.sass"

// Folder: Core
@import "./core/_base.sass"
@import "./core/_fonts.sass"
@import "./core/_variables.sass"
''')
    print('---------------------------------------')
    print(r'В папке [app/sass] успешно создан файл - style.sass')
    print(r'А также файлы - _fonts.sass, _variables.sass, _base.sass, _grid.sass')
    print(r'_smart-grid.sass, _smart-grid-percentage.sass, _smart-grid-rem.sass, _grid.sass')
    # TODO создание файла index.pug
    with open(fr'{get_directory}/app/pug/index.pug', 'w', encoding='utf8') as pug_file:
        pug_file.write('''doctype html
html
  head
    meta(charset="utf-8")
    title NAME-PROGECT
    link(rel="stylesheet", href="./css/style.css") 
  body
    ''')
    print('---------------------------------------')
    print(r'В папке [app/pug] успешно создан файл - index.pug')
    with open(fr'{get_directory}/app/js/script.js', 'w', encoding='utf8') as script_file:
        script_file.write(''''use strict';
/* global window */

window.onload = function () {
  //import * as checkCalc from './functions/check-calc.js';
}
''')
    with open(fr'{get_directory}/app/js/functions/check-calc.js', 'w', encoding='utf8') as script_file:
        script_file.write(''''use strict';
/* global document */

export default (function () {
    let div = document.createElement('div');
    let style = document.createElement('style');
    style.setAttribute('rel', 'stylesheet');
    div.style.width = 'calc(100%)';
    if (div.style.length > 0) { 
      style.setAttribute('href', './css/style.css');
    } else {
      style.setAttribute('href', './css/style-percentage.css');
    }
    document.body.appendChild(style);
}())
''')
    print('---------------------------------------')
    print(r'В папке [app/js] успешно созданы файлы - script.js, check-calc.js')
    print('---------------------------------------')
    print('Первоночальная инициализация проекта прошла успешно')
    main()


# TODO инициализация gulp-проекта
def gulp_prodject():
    if not os.path.isdir(fr'{get_directory}/gulp'):
        os.mkdir(fr'{get_directory}/gulp')
    # TODO создание файла gulpfile.js
    with open(os.path.join(get_directory, 'gulpfile.js'), 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();

const path = require('./gulp/path.js');
const htmlmin = require('./gulp/pug.js');
const font = require('./gulp/font.js');
const image = require('./gulp/image.js');
const style = require('./gulp/style.js');
const script = require('./gulp/script.js');
const clean = require('./gulp/clean.js');
const github = require('./gulp/github.js');
const sprite = require('./gulp/sprite.js');
const smartGrid = require('./gulp/smart-grid.js');

function watch() {
  browserSync.init({ server: { baseDir: path.baseDir, }, browser: path.browsers.firefox });
  gulp.watch(path.styles.app, style);
  gulp.watch(path.scripts.app, script);
  gulp.watch(path.pug.app, htmlmin);
  gulp.watch(path.images.appAll, gulp.series(sprite, image));
  gulp.watch(path.fonts.app, font);
};

gulp.task('html', htmlmin);
gulp.task('style', style);
gulp.task('script', script);
gulp.task('image', gulp.series(sprite, image));
gulp.task('font', font);
gulp.task('default', gulp.series(clean, sprite, gulp.parallel(image, style, script, htmlmin, font), watch));
gulp.task('del', gulp.series(clean, sprite, gulp.parallel(image, style, script, htmlmin, font)));
gulp.task('deploy', github);
gulp.task('smartgrid', smartGrid);
''')
    print('---------------------------------------')
    print('Файл gulp - gulplfile.js успешно создан')
    # TODO создание файла path.js
    with open(fr"{get_directory}/gulp/path.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global module */

// true - финальный, false - разработка
const isProduction = false;
// Нкжно ли составлять sourcemap для скриптов и стилей  
const sourceMap = false;

module.exports = {
  'isProd': isProduction,
  'sMap': sourceMap,
  'styles': {
    'app': './app/sass/style*.sass',
    'dist': './dist/css'
  },
  'scripts': {
    'app': './app/js/**/*.js',
    'dist': './dist/js'
  },
  'pug': {
    'app': './app/pug/*.pug',
    'dist': './dist'
  },
  'images': {
    'app': [
      './app/img/**/*.+(jpg|jpeg)',
      './app/img/sprit?.png',
      '!./app/img/maket*.*'
    ],
    'appAll': './app/img/**/*.+(jpg|jpeg|png)',
    'dist': './dist/img'
  },
  'sprite': {
    'app': './app/img/**/*.png',
    'distImg': './app/img',
    'distSass': './app/sass/sprite'
  },
  'fonts': {
    'app': './app/fonts/**/*.ttf',
    'dist': './dist/fonts'
  },
  'baseDir': './dist',
  'github': './dist/**/*',
  'maps': './map',
  'browsers': {
    'firefox': 'firefox developer edition',
    'chrome': 'google chrome',
    'safari': 'safari'
  },
  'path': __dirname
};
''')
    # TODO создание файла script.js
    with open(fr"{get_directory}/gulp/script.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global module, require */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const webpack = require('webpack-stream');

const path = require('./path.js');
const webConfig = require('./webpack.js');

module.exports = function() {
  return gulp.src(path.scripts.app)
    .pipe(webpack(webConfig))
    .pipe(gulp.dest(path.scripts.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла webpack.js
    with open(fr"{get_directory}/gulp/webpack.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global module, require */

const path = require('./path.js');

module.exports = {
  output: {
    filename: 'script.js'
  },
  module: {
    rules: [
      {
        test: /\.js$/,
        loader: 'babel-loader',
        exclude: '/node_modules/'
      }
    ]
  },
  devtool: path.sMap ? 'source-map' : 'none',
  mode: path.isProd ? 'production' : 'development'
};
''')
    # TODO создание файла image.js
    with open(fr"{get_directory}/gulp/image.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const image = require('gulp-image');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.images.app)
    .pipe(image({
      pngquant: ['--speed=1', '--force', 256],
      mozjpeg: ['-quality', 75]
    }))
    .pipe(gulp.dest(path.images.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла style.js
    with open(fr"{get_directory}/gulp/style.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create();
const autoprefixer = require('gulp-autoprefixer');
const cleanCSS = require('gulp-clean-css');
const gcmq = require('gulp-group-css-media-queries');
const uncss = require('gulp-uncss');
const gulpif = require('gulp-if');
const sourcemaps = require('gulp-sourcemaps');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.styles.app)
    .pipe(gulpif(path.sMap, sourcemaps.init({ loadMaps: true })))
    .pipe(sass().on('error', sass.logError))
    .pipe(gulpif(path.isProd, uncss({
      html: [`${path.pug.dist}/**/*.html`]
    })))
    .pipe(gcmq())
    .pipe(gulpif(path.isProd, autoprefixer({ browsers: ['> 0.1%'], cascade: false })))
    .pipe(gulpif(path.isProd, cleanCSS({ level: 2 })))
    .pipe(gulpif(path.sMap, sourcemaps.write(path.maps)))
    .pipe(gulp.dest(path.styles.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла clean.js
    with open(fr"{get_directory}/gulp/clean.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const del = require('del');

const path = require('./path.js')

module.exports = function() {
  return del([path.baseDir])
};
''')
    # TODO создание файла font.js
    with open(fr"{get_directory}/gulp/font.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const fs = require('fs');

const path = require('./path.js');

module.exports = function() { 
  const fd = fs.openSync(`${path.path}/../app/sass/core/_fonts.sass`, 'w+');
  const folder = fs.readdirSync(`${path.path}/../app/fonts`);
  for (let file of folder) {
    fs.writeFileSync(fd, `@font-face\\n  font-family: "${file.split('.')[0]}"\\n  src: url("../fonts/${file}")\\n$${file.split('.')[0].split('-').pop()}: ${file.split('.')[0]}\\n\\n`, { flag: 'a' });
  };
  return gulp.src(path.fonts.app)
    .pipe(gulp.dest(path.fonts.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла pug.js
    with open(fr"{get_directory}/gulp/pug.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const pug = require('gulp-pug');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.pug.app)
    .pipe(pug().on('error', console.log))
    .pipe(gulp.dest(path.pug.dist))
    .pipe(browserSync.stream())
};
''')
    with open(fr"{get_directory}/gulp/github.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module */

const gulp = require('gulp');
const ghPages = require('gulp-gh-pages');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.github)
    .pipe(ghPages());
};
''')
    with open(fr"{get_directory}/gulp/sprite.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module, console */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const image = require('gulp-image');
const spritesmith = require('gulp.spritesmith');
const merge = require('merge-stream');
const fs = require('fs');

const path = require('./path.js');

module.exports = function() {
  // Если есть, удаляем файл с именем sprite.png
  fs.unlink(`${path.path}/../${path.sprite.distImg}/sprite.png`, function(err){
    if(err) {
      console.log(err);
    } else {
      console.log(`File sprite.png is deleted`);
    }
  });
  let spriteData = gulp.src(path.sprite.app)
    .pipe(spritesmith({
      imgName: 'sprite.png',
      cssName: '_sprite.sass',
      cssFormat: 'sass',
      algoritm: 'binary-tree',
      cssTemplate: './gulp/sprite.mustache',
      cssVarMap: function(sprite) {
        sprite.name = 's-' + sprite.name;
      }
    }).on('error', console.log));
  // Сохранение спрайта (png)
  let imgStream = spriteData.img
    .pipe(gulp.dest(path.sprite.distImg));
  // Сохранение sass файла
  let sassStream = spriteData.css
    .pipe(gulp.dest(path.sprite.distSass));
  // Запуск gulp таска оновременно для спрайта и sass
  return merge(imgStream, sassStream)
    .on('error', console.log)
    .pipe(browserSync.stream())
};
''')
    with open(fr"{get_directory}/gulp/smart-grid.js", 'w', encoding='utf8') as gulp_file:
        gulp_file.write(''''use strict';
/* global require, module, console */

const { exec } = require('child_process');

module.exports = function() {
  return exec('node smart-grid-config.js', function(error, stdout, stderr) {
    if (error) {
      console.log(error);
    } else {
      console.log(stdout);
    }
  })
}
''')
    with open(fr"{get_directory}/gulp/sprite.mustache", 'w', encoding='utf8') as mustache_file:
        mustache_file.write('''{{#items}}
${{name}}: {{px.x}} {{px.y}} {{px.offset_x}} {{px.offset_y}} {{px.width}} {{px.height}} {{px.total_width}} {{px.total_height}} "{{{escaped_image}}}"
{{/items}}
''')
    print('---------------------------------------')
    print('В папке [gulp] - успешно созданы файлы: clean.js,')
    print('font.js, hpug.js, image.js, path.js, script.js, style.js, gpages.js') 
    print('sprite.js, smart-grid.js, sprite.mustache')
    #TODO Создание папки app/sass/sprite и в ней файла _mixins.sass
    if not os.path.isdir(fr'{get_directory}/app/sass/sprite'):
      os.mkdir(fr'{get_directory}/app/sass/sprite')
    with open(fr"{get_directory}/app/sass/sprite/_mixins.sass", 'w', encoding='utf8') as sass_file:
        sass_file.write('''@mixin spriteWidth($sprite)
  width: nth($sprite, 5)

@mixin spriteHeight($sprite)
  height: nth($sprite, 6)

@mixin spritePosition($sprite)
  background-position: nth($sprite, 3) nth($sprite, 4)

@mixin spriteImage($sprite)
  background-image: url("../img/#{nth($sprite, 9)}")

@mixin sprite($sprite)
  @include spriteImage($sprite)
  @include spritePosition($sprite)
  @include spriteWidth($sprite)
  @include spriteHeight($sprite)
''')
    with open(fr'{get_directory}/app/sass/sprite/_sprite.sass', 'w', encoding='utf8') as sass_file:
        pass
    print('---------------------------------------')
    print('В папке [app/sass/sprite] - успешно созданы файлы _mixins.sass и _sprite.sass')
    with open(fr'{get_directory}/app/sass/style.sass', 'a', encoding='utf8') as sass_file:
        sass_file.write('''\n// Folder: Sprite
@import "./sprite/_sprite.sass"
@import "./sprite/_mixins.sass"
''')
    main()


# TODO инициализация webpack-проекта
def webpack_prodject():
    if not os.path.isdir(fr'{get_directory}/webpack'):
        os.mkdir(fr'{get_directory}/webpack')
    # TODO создание консольных комманд webpack
    with open(fr"{get_directory}/package.json", 'r', encoding='utf8') as json_file:
        data_json = json.load(json_file)
    data_json['scripts'] = {
        'wpProduction': 'webpack --mode production',
        'wpDevelopment': 'webpack-dev-server --open --mode development',
    }
    with open(fr"{get_directory}/package.json", 'w', encoding='utf8') as json_file:
        json.dump(data_json, json_file, indent=4, ensure_ascii=False)
    # TODO создание файла webpack.config.js
    with open(fr"{get_directory}/webpack.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global require, module */

const argv = require('yargs').argv;
const CleanWebpackPlugin = require('clean-webpack-plugin');
const merge = require('webpack-merge');

const PATHS = require('./webpack/path.config.js');
const pug = require('./webpack/pug.config.js');
const sass = require('./webpack/sass.config.js');
const imgAndFont = require('./webpack/imageAndFonts.config.js');
const js = require('./webpack/js.config.js');

const isDevelopment = argv.mode === 'development';

module.exports = merge([
  {
  entry: PATHS.app,
  output: {
    filename: PATHS.FILENAME.js,
    path: PATHS.dist,
    publicPath: '/'
  },
  plugins: [
    new CleanWebpackPlugin(),
  ].concat(PATHS.generateHtmlPlugins(PATHS.pug)),
  devtool: isDevelopment ? 'source-map' : 'none',
  devServer: {
    contentBase: PATHS.dist,
    port: 8088,
    open: 'firefox',
    overlay: true
  }},
  js(),
  pug(isDevelopment),
  sass(),
  imgAndFont()
]);
''')
    print('---------------------------------------')
    print('Файл webpack - webpack.config.js успешно создан')
    # TODO создание файла imageAndFonts.config.js
    with open(fr"{get_directory}/webpack/imageAndFonts.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global require, module */

const CopyWebpackPlugin = require('copy-webpack-plugin');
const PATHS = require('./path.config.js');

module.exports = function() {
  return {
    module: {
      rules: [
        {
          test: /\.(png|jpg|gif|svg)$/,
          loader: 'file-loader',
          options: {
            name: '[name].[ext]'
          },
          exclude: '/node_modules/'
        }
      ]
    },
    plugins: [
      new CopyWebpackPlugin([{
        from: PATHS.fromImg,
        to: PATHS.toImg
      },
      {
        from: PATHS.fromFont,
        to: PATHS.toFont
      }])
    ]
  }
}
''')
    # TODO создание файла js.config.js
    with open(fr"{get_directory}/webpack/js.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global module */

module.exports = function() {
  return {
    module: {
      rules: [
        {
          test: /\.js$/,
          loader: 'babel-loader',
          exclude: '/node_modules/'
        }
      ]
    }
  }
}
''')
    # TODO создание файла path.config.js
    with open(fr"{get_directory}/webpack/path.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global require, module */

const path = require('path');
const fs = require('fs');
const HtmlWebpackPlugin = require('html-webpack-plugin');

module.exports = {
  app: [
    './app/js/index.js',
    './app/sass/index.sass',
  ],
  dist: `${path.resolve()}/dist`,
  pug: './app/pug',
  fromImg: './app/img',
  toImg: './dist/img',
  fromFont: './app/fonts',
  toFont: './dist/fonts',
  FILENAME: {
    js: './js/script.min.js',
    css: './css/style.min.css',
  },
  generateHtmlPlugins: function (templateDir) {
    const templateFiles = fs.readdirSync(`${path.resolve()}/${templateDir}`);
    return templateFiles.map(item => {
      const parts = item.split('.');
      const name = parts[0];
      const extension = parts[1];
      return new HtmlWebpackPlugin({
        filename: `${name}.html`,
        template: `${templateDir}/${name}.${extension}`,
        inject: false,
      })
    })
  }
};
''')
    # TODO создание файла postcss.config.js
    with open(fr"{get_directory}/webpack/postcss.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global module */

module.exports = {
  plugins: [
    require('autoprefixer')({
      browsers: ['> 0.1%'],
      cascade: false
      }
    ),
    require('css-mqpacker'),
    require('cssnano')({
      preset: [
        'default', {
          discardComments: {
            removeAll: true,
          }
        }
      ]
    })
  ]
}
''')
    # TODO создание файла pug.config.js
    with open(fr"{get_directory}/webpack/pug.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global module */

module.exports = function(isDevelopment) {
  return {
    module: {
      rules: [
        {
          test: /\.pug$/,
          loader: 'pug-loader',
          options: { pretty: isDevelopment }
        }
      ]
    }
  }
}
''')
    # TODO создание файла sass.config.js
    with open(fr"{get_directory}/webpack/sass.config.js", 'w', encoding='utf8') as webpack_file:
        webpack_file.write(''''use strict';
/* global require, module */

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const PATHS = require('./path.config.js');

module.exports = function() {
  return {
    module: {
      rules: [
        {
          test: /\.sass$/,
          use: [
            MiniCssExtractPlugin.loader,
            {
              loader: 'css-loader',
            },
            {
              loader: 'postcss-loader',
              options: {
                config: { path: './webpack/postcss.config.js' } 
              }
            },
            {
              loader: 'sass-loader',
            }
          ],
          exclude: '/node_modules/'
        }
      ]
    },
    plugins: [
      new MiniCssExtractPlugin({
        filename: PATHS.FILENAME.css
      }),
    ]
  }
}
''')
    print('В папке [webpack] - успешно созданы файлы:')
    print('sass.config.js, path.config.js, postcss.config.js')
    print('pug.config.js, js.config.js, imageAndFonts.config.js')
    main()


def main():
    print('---------------------------------------')
    print('0 - инициализация проекта')
    print('1 - инициализация gulp(& webpack)-проекта')
    print('2 - инициализация webpack-проекта')
    print('3 - выход')
    print('---------------------------------------')
    commands = input()
    commands.strip()
    if '0' in commands:
        dev_primary_progect()
    elif '1' in commands:
        gulp_prodject()
    elif '2' in commands:
        webpack_prodject()
    elif '3' in commands:
        exit


if __name__ == "__main__":
    main()
