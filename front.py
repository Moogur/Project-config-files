import os
import json

addDirectory = {
    'sass': ('grid', 'core', 'layout'),
    'js': ('functions', ),
    'img': bool,
    'fonts': bool,
    'pug': ('mixin', )
}
addFilePug = {
    'mixin': ('smartgrid.pug', )
}
addFileSass = {
  'core': ('_fonts.sass', '_base.sass', '_variables.sass', '_mixines.sass'),
  'grid': ('_grid.sass', )
}
symlinkNodeModules = r'/Users/dilkree/IT/JS_MODULES/node_modules'
getDirectory = os.getcwd()


def primaryProject():
    # TODO создание дерева папок для проекта
    for i in addDirectory:
        if type(addDirectory[i]) is tuple:
            for j in addDirectory[i]:
                os.makedirs(fr'{getDirectory}/app/{i}/{j}')
        else:
            os.mkdir(fr'{getDirectory}/app/{i}')
    # TODO создание символической ссылки на node_modules
    os.symlink(symlinkNodeModules, 'node_modules')
    print('---------------------------------------')
    print('Дерево каталогов проекта успешно создано')
    # TODO создание файла package.json
    if not os.path.isfile(os.path.join(getDirectory, 'package.json')):
        os.system('npm init -y')
    print('---------------------------------------')
    print('Файл package.json успешно создан')
    # TODO создание файла .babelrc
    with open(fr'{getDirectory}/.babelrc', 'w', encoding='utf8') as fileBabel:
        fileBabel.write('''{
"presets": [
  "@babel/preset-env",
]
}''')
    # TODO создание файла smart-grid-config.js
    with open(fr'{getDirectory}/smartgrid-config.js', 'w', encoding='utf-8') as fileSG:
        fileSG.write(''''use strict';

const smartgrid = require('/Users/dilkree/IT/JS_MODULES/my_modules/smart-grid');

// Базовый размер шрифта
const baseFontPx = '16px';

const settings = {
  filename: '_smartgrid',
  outputStyle: 'sass',
  columns: 12,
  offset: '20px', // Расстояние между столбцами (gutter)
  // false => max-width, true => min-width
  mobileFirst: false,
  container: {
    maxWidth: '1280px', // Ширина макета
    fields: '30px' // Оступы по краям сайта (padding)
  },
  breakPoints: {
    // Bootstrap breakPoints
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
    with open(fr'{getDirectory}/.gitignore', 'w', encoding='utf8') as fileGitIgnore:
        fileGitIgnore.write('''.DS_Store
/dist/
/gulp/
/node_modules
/.gitignore
/.babelrc
/package.json
/front.py
/gulpfile.js
/smartgrid-config.js
**/*.psd
**/maket*.jpg
*.txt''')
    print('---------------------------------------')
    print('Файлы: .babelrc, .gitignore, smartgrid-config.js успешно созданы')
    # TODO создание файлов *.sass
    for i in addFileSass:
        for j in addFileSass[i]:
            with open(fr'{getDirectory}/app/sass/{i}/{j}', 'w', encoding='utf8') as fileSass:
                    if j == '_grid.sass':
                        fileSass.write('''+reset()

.debug
  +debug(rgba(0, 0, 0, 0.2), 1px solid #ffff00)

.container
  +container()
''')
                    elif j == '_mixines.sass':
                        fileSass.write('''=font-face($fontFace, $expansion)
  @font-face          
    font-family: "#{$fontFace}"
    src: url("../fonts/#{$fontFace}.#{$expansion}")

=box($width, $height: $width)
  width: $width
  height: $height
''')
                    else:
                        pass
    with open(fr'{getDirectory}/app/sass/style.sass', 'w', encoding='utf8') as fileSass:
        fileSass.write('''// Folder: Grid
@import "./grid/_smartgrid.sass"
//@import "./grid/_smartgrid-percentage.sass"
//@import "./grid/_smartgrid-rem.sass"
@import "./grid/_grid.sass"

//Font icon
@import "/Users/dilkree/IT/JS_MODULES/my_modules/icon/_mixines.sass"

// Folder: Core
@import "./core/_fonts.sass"
@import "./core/_variables.sass"
@import "./core/_mixines.sass"
@import "./core/_base.sass"
''')
    print('---------------------------------------')
    print(r'В папке [app/sass] успешно создан файл - style')
    print(r'А также файлы - fonts, variables, base, grid')
    # TODO создание файла index.pug
    with open(fr'{getDirectory}/app/pug/index.pug', 'w', encoding='utf8') as filePug:
        filePug.write('''include ./mixin/smartgrid.pug
doctype html
html
  head
    meta(charset="utf-8")
    title NAME-PROGECT
    link(rel="stylesheet" href="./css/style.css")
  body
    ''')
    for i in addFilePug:
        for j in addFilePug[i]:
            with open(fr'{getDirectory}/app/pug/{i}/{j}', 'w', encoding='utf8') as filePug:
                    if j == 'smartgrid.pug':
                        filePug.write('''mixin debug12
  div.debug
    div
      div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div

mixin debug24
  div.debug
    div
      div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
        div
''')
    print('---------------------------------------')
    print(r'В папке [app/pug] успешно создан файл - index, smartgrid')
    with open(fr'{getDirectory}/app/js/script.js', 'w', encoding='utf8') as fileJS:
        fileJS.write(''''use strict';

// import {checkCalc} from './functions/check-calc.js';
''')
    with open(fr'{getDirectory}/app/js/functions/check-calc.js', 'w', encoding='utf8') as fileJS:
        fileJS.write(''''use strict';

function checkCalc () {
  window.onload =  function () {
    const div = document.createElement('div');
    const style = document.createElement('style');
    style.setAttribute('rel', 'stylesheet');
    div.style.width = 'calc(100%)';
    if (div.style.length > 0) {
      style.setAttribute('href', './css/style.css');
    } else {
      style.setAttribute('href', './css/style-percentage.css');
    };
    document.body.appendChild(style);
    console.log(1);
  }
};

export {checkCalc};
''')
    print('---------------------------------------')
    print(r'В папке [app/js] успешно созданы файлы - script.js, check-calc.js')
    with open (f'{getDirectory}/package.json', 'r', encoding='utf-8') as fileJSON:
        data = json.load(fileJSON)
    data['scripts'] = {
      'smartgrid': 'node smartgrid-config.js'
    }
    with open (f'{getDirectory}/package.json', 'w', encoding='utf-8') as fileJSON:
        json.dump(data, fileJSON, indent=2, ensure_ascii=False)


# TODO инициализация gulp-проекта
def gulpProject():
    if not os.path.isdir(fr'{getDirectory}/gulp'):
        os.mkdir(fr'{getDirectory}/gulp')
    # TODO создание файла gulpfile.js
    with open(os.path.join(getDirectory, 'gulpfile.js'), 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';

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

function watch() {
  browserSync.init({ server: { baseDir: path.baseDir, }, browser: path.browsers.firefox });
  gulp.watch(path.styles.appWatch, style);
  gulp.watch(path.scripts.appWatch, script);
  gulp.watch(path.pug.appWatch, htmlmin);
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
''')
    print('---------------------------------------')
    print('Файл gulp - gulplfile.js успешно создан')
    # TODO создание файла path.js
    with open(fr"{getDirectory}/gulp/path.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

// true - финальный, false - разработка
const isProduction = false;
// Нкжно ли составлять sourcemap для скриптов и стилей
const sourceMap = false;

module.exports = {
  'isProd': isProduction,
  'isMap': sourceMap,
  'styles': {
    'appWatch': './app/sass/**/*.sass',
    'app': './app/sass/style*.sass',
    'dist': './dist/css'
  },
  'scripts': {
    'appWatch': './app/js/**.*js',
    'app': './app/js/script*.js',
    'dist': './dist/js'
  },
  'pug': {
    'appWatch': './app/pug/**/*.pug',
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
    'app': './app/fonts/**/*.+(ttf|woff)',
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
    with open(fr"{getDirectory}/gulp/script.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

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
    with open(fr"{getDirectory}/gulp/webpack.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const path = require('./path.js');

module.exports = {
  output: {
    filename: 'script.js'
  },
  module: {
    rules: [
      {
        test: /\\.js$/,
        loader: 'babel-loader',
        exclude: '/node_modules/'
      }
    ]
  },
  devtool: path.isMap ? 'source-map' : 'none',
  mode: path.isProd ? 'production' : 'development'
};
''')
    # TODO создание файла image.js
    with open(fr"{getDirectory}/gulp/image.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

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
    with open(fr"{getDirectory}/gulp/style.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const gulp = require('gulp');
const sass = require('gulp-sass');
const browserSync = require('browser-sync').create();
const postcss = require('gulp-postcss');
const autoprefixer = require('autoprefixer');
const cssnano = require('cssnano');
const mqpacker = require('css-mqpacker');
const uncss = require('postcss-uncss');
const gulpif = require('gulp-if');
const sourcemaps = require('gulp-sourcemaps');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.styles.app)
    .pipe(gulpif(path.isMap, sourcemaps.init({ loadMaps: true })))
    .pipe(sass().on('error', sass.logError))
    .pipe(gulpif(path.isProd, postcss([
      uncss({html: [`${path.pug.dist}/**/*.html`]}),
      mqpacker(),
      autoprefixer({ browsers: ['> 0.1%'], cascade: false }),
      cssnano({preset: ['default', {
        discardComments: {removeAll: true}
      }]})
    ])))
    .pipe(gulpif(path.isMap, sourcemaps.write(path.maps)))
    .pipe(gulp.dest(path.styles.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла clean.js
    with open(fr"{getDirectory}/gulp/clean.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const del = require('del');

const path = require('./path.js')

module.exports = function() {
  return del([path.baseDir])
};
''')
    # TODO создание файла font.js
    with open(fr"{getDirectory}/gulp/font.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const gulp = require('gulp');
const ttf2woff = require('gulp-ttf2woff');
const browserSync = require('browser-sync').create();
const fs = require('fs');

const path = require('./path.js');

module.exports = function() {
  const fd = fs.openSync(`${path.path}/../app/sass/core/_fonts.sass`, 'w+');
  const folder = fs.readdirSync(`${path.path}/../app/fonts`);
  for (let file of folder) {
    fs.writeFileSync(fd, `@font-face\\n  font-family: "${file.split('.')[0]}"\\n  src: url("../fonts/${file.split('.')[0]}.woff")\\n$${file.split('.')[0].split('-').pop()}: ${file.split('.')[0]}\\n\\n`, { flag: 'a' });
  };
  return gulp.src(path.fonts.app)
    .pipe(ttf2woff())
    .pipe(gulp.dest(path.fonts.dist))
    .pipe(browserSync.stream())
};
''')
    # TODO создание файла pug.js
    with open(fr"{getDirectory}/gulp/pug.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const gulp = require('gulp');
const browserSync = require('browser-sync').create();
const pug = require('gulp-pug');
const pugbem =require('/Users/dilkree/IT/JS_MODULES/my_modules/gulp-pugbem');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.pug.app)
    .pipe(pug({
      pretty: false,
      plugins: [pugbem]
    }).on('error', console.log))
    .pipe(gulp.dest(path.pug.dist))
    .pipe(browserSync.stream())
};
''')
    with open(fr"{getDirectory}/gulp/github.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

const gulp = require('gulp');
const ghPages = require('gulp-gh-pages');

const path = require('./path.js');

module.exports = function() {
  return gulp.src(path.github)
    .pipe(ghPages());
};
''')
    with open(fr"{getDirectory}/gulp/sprite.js", 'w', encoding='utf8') as fileGulpJS:
        fileGulpJS.write(''''use strict';
/* global module */

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
    with open(fr"{getDirectory}/gulp/sprite.mustache", 'w', encoding='utf8') as fileMustache:
        fileMustache.write('''{{#items}}
${{name}}: {{px.x}} {{px.y}} {{px.offset_x}} {{px.offset_y}} {{px.width}} {{px.height}} {{px.total_width}} {{px.total_height}} "{{{escaped_image}}}"
{{/items}}
''')
    print('---------------------------------------')
    print('В папке [gulp] - успешно созданы файлы: clean.js,')
    print('font.js, hpug.js, image.js, path.js, script.js, style.js, gpages.js') 
    print('sprite.js, smartgrid.js, sprite.mustache')
    #TODO Создание папки app/sass/sprite и в ней файла _mixins.sass
    if not os.path.isdir(fr'{getDirectory}/app/sass/sprite'):
      os.mkdir(fr'{getDirectory}/app/sass/sprite')
    with open(fr"{getDirectory}/app/sass/sprite/_mixins.sass", 'w', encoding='utf8') as fileSass:
        fileSass.write('''@mixin spriteWidth($sprite)
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
    with open(fr'{getDirectory}/app/sass/sprite/_sprite.sass', 'w', encoding='utf8') as fileSass:
        pass
    print('---------------------------------------')
    print('В папке [app/sass/sprite] - успешно созданы файлы mixins и sprite')
    with open(fr'{getDirectory}/app/sass/style.sass', 'a', encoding='utf8') as fileSass:
        fileSass.write('''\n// Folder: Sprite
@import "./sprite/_sprite.sass"
@import "./sprite/_mixins.sass"

// Folder: Layout
''')


if __name__ == "__main__":
    primaryProject()
    gulpProject()
