import json
import os

addDirectory = {
    "sass": ("grid", "core", "layout"),
    "js": ("functions", ),
    "img": ("sprites", ),
    "fonts": bool,
    "pug": ("layout", )
}
addFilePug = {
    "layout": ("mixines.pug", "base.pug")
}
addFileSass = {
    "core": ("_fonts.sass", "_base.sass", "_variables.sass", "_mixines.sass"),
    "grid": ("_grid.sass", )
}
symlinkNodeModules = r"/Users/dilkree/IT/JS_MODULES/node_modules"
getDirectory = os.getcwd()


def primaryProject():
    # TODO создание дерева папок для проекта
    for i in addDirectory:
        if type(addDirectory[i]) is tuple:
            for j in addDirectory[i]:
                os.makedirs(fr"{getDirectory}/src/{i}/{j}")
        else:
            os.mkdir(fr"{getDirectory}/src/{i}")
    # TODO Создание файла .vscode/settings.json
    spyFiles = {
        "files.exclude": {
            "**/node_modules": "true",
            "package.json": "true",
            ".gitignore": "true",
            "LICENSE": "true",
            "license": "true",
            "*.md": "true",
            "front.py": "true",
            "*.studio": "true",
            "*.psd": "true",
            "*.sketch": "true"
        }
    }
    if not os.path.isdir(fr"{getDirectory}/.vscode/"):
        os.mkdir(fr"{getDirectory}/.vscode/")
    with open(fr"{getDirectory}/.vscode/settings.json", "w", encoding="utf-8") as fileJSON:
        json.dump(spyFiles, fileJSON, indent=4, ensure_ascii=False)
    # TODO создание символической ссылки на node_modules
    os.symlink(symlinkNodeModules, "node_modules")
    print("---------------------------------------")
    print("Дерево каталогов проекта успешно создано")
    # TODO создание файла package.json
    if not os.path.isfile(os.path.join(getDirectory, "package.json")):
        os.system("npm init -y")
    print("---------------------------------------")
    print("Файл package.json успешно создан")
    # TODO создание файла smart-grid-config.js
    with open(fr"{getDirectory}/smartgrid-config.js", "w", encoding="utf-8") as fileSG:
        fileSG.write(""""use strict";

const smartgrid = require("/Users/dilkree/IT/JS_MODULES/my_modules/smart-grid");
const folderPath = "./src/sass/grid";

const settings = {
    filename: "_smartgrid",
    outputStyle: "sass",
    columns: 12,
    offset: "20px", // Расстояние между столбцами (gutter)
    // false => max-width, true => min-width
    mobileFirst: false,
    container: {
        maxWidth: "1280px", // Ширина макета
        // Оступы по краям сайта (padding)
        // fields должен быть не меньше половины offset
        fields: "30px"
    },
    breakPoints: {
        // Bootstrap breakPoints
        xl: {
            width: "1200px",
            fields: "30px"
        },
        lg: {
            width: "992px",
            fields: "16px"
        },
        md: {
            width: "768px",
            fields: "24px"
        },
        sm: {
            width: "576px",
            fields: "18px"
        }
    },
    mixinNames: {
        container: "container",
        shift: "offset"
    },
    tab: "  "
};

const arr = [undefined, {
    filename: settings.filename + "-percentage",
    offset: (parseInt(settings.offset) / parseInt(settings.container.maxWidth) * 100) + "%"
}];

for (let value of arr) {
    smartgrid(folderPath, Object.assign(settings, value));
}
""")
    with open(fr"{getDirectory}/.gitignore", "w", encoding="utf8") as fileGitIgnore:
        fileGitIgnore.write(""".DS_Store
/.vscode/
/dist/
/gulp/
/node_modules
/front.py
/gulpfile.js
/smartgrid-config.js
**/*.psd
**/*.studio
**/*.sketch
**/*.txt""")
    print("---------------------------------------")
    print("Файлы: .gitignore, smartgrid-config.js успешно созданы")
    # TODO создание файлов *.sass
    for i in addFileSass:
        for j in addFileSass[i]:
            with open(fr"{getDirectory}/src/sass/{i}/{j}", "w", encoding="utf8") as fileSass:
                if j == "_grid.sass":
                    fileSass.write("""@import "./_smartgrid.sass"
//@import "./_smartgrid-percentage.sass"

+reset()

.debug
    +debug(rgba(0, 0, 0, 0.2), 1px solid #ffff00)

.container
    +container()
""")
                elif j == "_mixines.sass":
                    fileSass.write("""=font-face($fontFace, $expansion)
    @font-face
        font-family: "#{$fontFace}"
        src: url("../fonts/#{$fontFace}.#{$expansion}")

=box($width, $height: $width)
    width: $width
    height: $height
""")
                else:
                    pass
    with open(fr"{getDirectory}/src/sass/style.sass", "w", encoding="utf8") as fileSass:
        fileSass.write("""// Folder: Grid
@import "./grid/_grid.sass"

//Font icon
//@import "/Users/dilkree/IT/JS_MODULES/my_modules/icons/_mixines.sass"

// Folder: Core
@import "./core/_fonts.sass"
@import "./core/_variables.sass"
@import "./core/_mixines.sass"
@import "./core/_base.sass"
""")
    print("---------------------------------------")
    print(r"В папке [src/sass] успешно создан файл - style")
    print(r"А также файлы - fonts, variables, base, grid")
    # TODO создание файла index.pug
    with open(fr"{getDirectory}/src/pug/index.pug", "w", encoding="utf8") as filePug:
        filePug.write("""extends ./layout/base.pug

block style
    link(rel="stylesheet" href="css/style.css")

block title
    title Заголовок страницы

block bodyContent
""")
    for i in addFilePug:
        for j in addFilePug[i]:
            with open(fr"{getDirectory}/src/pug/{i}/{j}", "w", encoding="utf8") as filePug:
                if j == "mixines.pug":
                    filePug.write("""mixin debug12
    div.debug
        div
            div
                - let n = 0;
                while n < 12
                    div
                    - n++;

mixin debug24
    div.debug
        div
            div
                - let n = 0;
                while n < 24
                    div
                    - n++;
""")
                if j == "base.pug":
                    filePug.write("""include ./mixines.pug
doctype html
html(lang="ru")
    head
        meta(charset="utf-8")
        meta(name="viewport", content="width=device-width, initial-scale=1.0")
        meta(http-equiv="X-UA-Compatible", content="ie=edge")
        block title
        block style
    body
        block bodyContent
""")
    print("---------------------------------------")
    print(r"В папке [src/pug] успешно создан файл - index, smartgrid")
    with open(fr"{getDirectory}/src/js/main.js", "w", encoding="utf8") as fileJS:
        fileJS.write(""""use strict";

// const {checkCalc} = require("/Users/dilkree/IT/JS_MODULES/my_modules/my_javascript/function/check-calc.js");
""")
    print("---------------------------------------")
    print(r"В папке [src/js] успешно созданы файлы - main.js")
    with open(f"{getDirectory}/package.json", "r", encoding="utf-8") as fileJSON:
        data = json.load(fileJSON)
    data["scripts"] = {
        "smartgrid": "node smartgrid-config.js",
        "Development": "gulp",
        "Production": "gulp del --prod"
    }
    data["browsers"] = [
        "> 0.1%"
    ]
    data["devDependencies"] = {
        "@babel/core": "^7.4.5",
        "@babel/preset-env": "^7.4.5",
        "autoprefixer": "^9.6.0",
        "babel-loader": "^8.0.6",
        "browser-sync": "^2.26.7",
        "css-mqpacker": "^7.0.0",
        "cssnano": "^4.1.10",
        "del": "^3.0.0",
        "gulp": "^4.0.2",
        "gulp-changed": "^4.0.0",
        "gulp-gh-pages": "^0.5.4",
        "gulp-if": "^2.0.2",
        "gulp-image": "^5.1.0",
        "gulp-postcss": "^8.0.0",
        "gulp-pug": "^4.0.1",
        "gulp-pugbem": "^2.2.4",
        "gulp-sass": "^4.0.2",
        "gulp-selectors": "^0.1.10",
        "gulp-sourcemaps": "^2.6.5",
        "gulp-ttf2woff": "^1.1.1",
        "gulp.spritesmith": "^6.10.1",
        "merge-stream": "^1.0.1",
        "mozjpeg": "^6.0.1",
        "node-sass": "^4.12.0",
        "pngquant": "^2.0.1",
        "postcss-uncss": "^0.16.1",
        "smart-grid": "^2.1.2",
        "uncss": "^0.16.2",
        "webpack-stream": "^5.2.1"
    }
    data["dependencies"] = {
        "jquery": "^3.4.1"
    }
    with open(f"{getDirectory}/package.json", "w", encoding="utf-8") as fileJSON:
        json.dump(data, fileJSON, indent=4, ensure_ascii=False)


# TODO инициализация gulp-проекта
def gulpProject():
    if not os.path.isdir(fr"{getDirectory}/gulp"):
        os.mkdir(fr"{getDirectory}/gulp")
    # TODO создание файла gulpfile.js
    with open(os.path.join(getDirectory, "gulpfile.js"), "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const browserSync = require("browser-sync").create();

const path = require("./gulp/path.js");
const htmlmin = require("./gulp/pug.js");
const font = require("./gulp/font.js");
const image = require("./gulp/image.js");
const style = require("./gulp/style.js");
const script = require("./gulp/script.js");
const clean = require("./gulp/clean.js");
const github = require("./gulp/github.js");
const sprite = require("./gulp/sprite.js");


function watch() {
    browserSync.init({ server: { baseDir: path.baseDir }, browser: path.browsers.chrome });
    gulp.watch(path.styles.srcWatch, style);
    gulp.watch(path.scripts.srcWatch, script);
    gulp.watch(path.pug.srcWatch, htmlmin);
    gulp.watch(path.images.srcAll, gulp.series(sprite, image));
    gulp.watch(path.fonts.src, font);
}


gulp.task("html", htmlmin);
gulp.task("style", style);
gulp.task("script", script);
gulp.task("image", gulp.series(sprite, image));
gulp.task("font", font);
gulp.task("del", gulp.series(clean, sprite, htmlmin, font, gulp.parallel(image, style, script)));
gulp.task("default", gulp.series("del", watch));
gulp.task("deploy", github);
""")
    print("---------------------------------------")
    print("Файл gulp - gulplfile.js успешно создан")
    # TODO создание файла path.js
    with open(fr"{getDirectory}/gulp/path.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";
/* global __dirname process */

module.exports = {
    "isDev": !(process.argv.indexOf("--prod") !== -1),
    "isProd": (process.argv.indexOf("--prod") !== -1),
    "styles": {
        "srcWatch": "./src/sass/**/*.sass",
        "src": "./src/sass/style*.sass",
        "dist": "./dist/css"
    },
    "scripts": {
        "srcWatch": "./src/js/**.*js",
        "src": "./src/js/main*.js",
        "dist": "./dist/js"
    },
    "pug": {
        "srcWatch": "./src/pug/**/*.pug",
        "src": "./src/pug/*.pug",
        "dist": "./dist"
    },
    "images": {
        "src": [
            "./src/img/**/*.+(jpg|jpeg|png)",
            "!./src/img/sprites"
        ],
        "srcAll": "./src/img/**/*.+(jpg|jpeg|png)",
        "dist": "./dist/img"
    },
    "sprite": {
        "src": "./src/img/sprites/*.png",
        "distImg": "src/img",
        "distSass": "./src/sass/sprite"
    },
    "fonts": {
        "src": "./src/fonts/**/*.+(ttf|woff|otf)",
        "dist": "./dist/fonts"
    },
    "baseDir": "./dist",
    "github": "./dist/**/*",
    "browsers": {
        "firefox": "firefox developer edition",
        "chrome": "google chrome"
    },
    "path": __dirname
};
""")
    # TODO создание файла script.js
    with open(fr"{getDirectory}/gulp/script.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const webpack = require("webpack-stream");
const changed = require("gulp-changed");

const path = require("./path.js");
const webConfig = require("./webpack.js");

module.exports = function() {
    return gulp.src(path.scripts.src)
        .pipe(changed(path.scripts.dist))
        .pipe(webpack(webConfig))
        .pipe(gulp.dest(path.scripts.dist))
        .pipe(browserSync.stream());
};
""")
    # TODO создание файла webpack.js
    with open(fr"{getDirectory}/gulp/webpack.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const path = require("./path.js");

module.exports = {
    output: {
        filename: "[name].js"
    },
    module: {
        rules: [
            {
                test: /\\.js$/,
                loader: "babel-loader",
                options: {
                    presets: ["@babel/preset-env"],
                    plugins: [
                        "@babel/plugin-proposal-class-properties"
                    ]
                },
                exclude: "/node_modules/"
            }
        ]
    },
    devtool: path.isProd ? "none" : "cheap-module-eval-source-map",
    mode: path.isProd ? "production" : "development"
};
""")
    # TODO создание файла image.js
    with open(fr"{getDirectory}/gulp/image.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const image = require("gulp-image");
const changed = require("gulp-changed");

const path = require("./path.js");

module.exports = function() {
    return gulp.src(path.images.src)
        .pipe(changed(path.images.dist))
        .pipe(image({
            pngquant: ["--speed=1", "--force", 256],
            mozjpeg: ["-quality", 75]
        }))
        .pipe(gulp.dest(path.images.dist))
        .pipe(browserSync.stream());
};
""")
    # TODO создание файла style.js
    with open(fr"{getDirectory}/gulp/style.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const sass = require("gulp-sass");
const browserSync = require("browser-sync").create();
const postcss = require("gulp-postcss");
const autoprefixer = require("autoprefixer");
const cssnano = require("cssnano");
const mqpacker = require("css-mqpacker");
const uncss = require("postcss-uncss");
const gulpif = require("gulp-if");
const sourcemaps = require("gulp-sourcemaps");
const changed = require("gulp-changed");

const path = require("./path.js");

module.exports = function() {
    return gulp.src(path.styles.src)
        .pipe(changed(path.styles.dist))
        .pipe(gulpif(path.isDev, sourcemaps.init()))
        .pipe(sass({
            outputStyle: "expanded"
        }).on("error", sass.logError))
        .pipe(gulpif(path.isProd, postcss([
            uncss({html: [`${path.pug.dist}/**/*.html`]}),
            mqpacker(),
            autoprefixer(),
            cssnano({preset: ["default", {
                discardComments: {removeAll: true}
            }]})
        ])))
        .pipe(sourcemaps.write())
        .pipe(gulp.dest(path.styles.dist))
        .pipe(browserSync.stream());
};
""")
    # TODO создание файла clean.js
    with open(fr"{getDirectory}/gulp/clean.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const del = require("del");

const path = require("./path.js");

module.exports = function() {
    return del([path.baseDir]);
};
""")
    # TODO создание файла font.js
    with open(fr"{getDirectory}/gulp/font.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const ttf2woff = require("gulp-ttf2woff");
const browserSync = require("browser-sync").create();
const fs = require("fs");
const changed = require("gulp-changed");

const path = require("./path.js");

module.exports = function() {
    const fd = fs.openSync(`${path.path}/../src/sass/core/_fonts.sass`, "w+");
    const folder = fs.readdirSync(`${path.path}/../src/fonts`);
    for (let file of folder) {
        if (["ttf", "woff", "otf"].indexOf(file.split(".")[1]) != -1) {
            fs.writeFileSync(fd, `@font-face\n  font-family: "${file.split(".")[0]}"\n  src: url("../fonts/${file.split(".")[0]}.woff")\n$${file.split(".")[0]}: ${file.split(".")[0]}\n\n`, { flag: "a" });
        }
    }
    return gulp.src(path.fonts.src)
        .pipe(changed(path.fonts.dist))
        .pipe(ttf2woff())
        .pipe(gulp.dest(path.fonts.dist))
        .pipe(browserSync.stream());
};
""")
    # TODO создание файла pug.js
    with open(fr"{getDirectory}/gulp/pug.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const pug = require("gulp-pug");
const pugbem =require("/Users/dilkree/IT/JS_MODULES/my_modules/gulp-pugbem");

const path = require("./path.js");

module.exports = function() {
    return gulp.src(path.pug.src)
        .pipe(pug({
            pretty: path.isProd ? false : true,
            plugins: [pugbem]
        }).on("error", console.log))
        .pipe(gulp.dest(path.pug.dist))
        .pipe(browserSync.stream());
};
""")
    with open(fr"{getDirectory}/gulp/github.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const ghPages = require("gulp-gh-pages");

const path = require("./path.js");

module.exports = function() {
    return gulp.src(path.github)
        .pipe(ghPages());
};
""")
    with open(fr"{getDirectory}/gulp/sprite.js", "w", encoding="utf8") as fileGulpJS:
        fileGulpJS.write(""""use strict";

const gulp = require("gulp");
const browserSync = require("browser-sync").create();
const spritesmith = require("gulp.spritesmith");
const merge = require("merge-stream");
const fs = require("fs");

const path = require("./path.js");

module.exports = function() {
    // Если есть, удаляем файл с именем sprite.png
    fs.unlink(`${path.path}/../${path.sprite.distImg}/sprite.png`, function(err){
        if(err) {
            console.log(err);
        } else {
            console.log(`File sprite.png is deleted`);
        }
    });
    let spriteData = gulp.src(path.sprite.src)
        .pipe(spritesmith({
            imgName: "sprite.png",
            cssName: "_sprite.sass",
            cssFormat: "sass",
            algoritm: "binary-tree",
            cssTemplate: "./gulp/sprite.mustache",
            cssVarMap: function(sprite) {
                sprite.name = "s-" + sprite.name;
            }
        }).on("error", console.log));
    // Сохранение спрайта (png)
    let imgStream = spriteData.img
        .pipe(gulp.dest(path.sprite.distImg));
    // Сохранение sass файла
    let sassStream = spriteData.css
        .pipe(gulp.dest(path.sprite.distSass));
    // Запуск gulp таска оновременно для спрайта и sass
    return merge(imgStream, sassStream)
        .on("error", console.log)
        .pipe(browserSync.stream());
};
""")
    with open(fr"{getDirectory}/gulp/sprite.mustache", "w", encoding="utf8") as fileMustache:
        fileMustache.write("""{{#items}}
${{name}}: {{px.x}} {{px.y}} {{px.offset_x}} {{px.offset_y}} {{px.width}} {{px.height}} {{px.total_width}} {{px.total_height}} "{{{escaped_image}}}"
{{/items}}
""")
    print("---------------------------------------")
    print("В папке [gulp] - успешно созданы файлы: clean.js,")
    print("font.js, hpug.js, image.js, path.js, script.js, style.js, gpages.js")
    print("sprite.js, smartgrid.js, sprite.mustache")
    # TODO Создание папки src/sass/sprite и в ней файла _mixins.sass
    if not os.path.isdir(fr"{getDirectory}/src/sass/sprite"):
        os.mkdir(fr"{getDirectory}/src/sass/sprite")
    with open(fr"{getDirectory}/src/sass/sprite/_mixins.sass", "w", encoding="utf8") as fileSass:
        fileSass.write("""@mixin spriteWidth($sprite)
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
""")
    with open(fr"{getDirectory}/src/sass/sprite/_sprite.sass", "w", encoding="utf8") as fileSass:
        pass
    print("---------------------------------------")
    print("В папке [src/sass/sprite] - успешно созданы файлы mixins и sprite")
    with open(fr"{getDirectory}/src/sass/style.sass", "a", encoding="utf8") as fileSass:
        fileSass.write("""\n// Folder: Sprite
@import "./sprite/_sprite.sass"
@import "./sprite/_mixins.sass"

// Folder: Layout
""")


if __name__ == "__main__":
    primaryProject()
    gulpProject()
