from flask import Flask, render_template_string

app = Flask(__name__)

HTML = r"""
<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Edjie's Birthday Quest</title>

<style>
:root{
    --bg:#030817;
    --blue:#238cff;
    --cyan:#79e7ff;
    --purple:#9a79ff;
    --white:#f4f8ff;
}

*{box-sizing:border-box}
html{scroll-behavior:smooth}

body{
    margin:0;
    font-family:"Courier New",monospace;
    color:var(--white);
    background:transparent;
    overflow-x:hidden;
}

button,input{font:inherit}
.hidden{display:none!important}

body:after{
    content:"";
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:9999;
    background:
        repeating-linear-gradient(
            to bottom,
            rgba(255,255,255,.018) 0 2px,
            transparent 2px 5px
        );
}

/* =========================================================
   ANIMATED GRADIENT BACKGROUND
========================================================= */

.animated-gradient-bg{
    position:fixed;
    inset:0;
    z-index:-5;
    background:
        linear-gradient(
            135deg,
            #030817,
            #0b2b67,
            #1762d7,
            #3d8cff,
            #6456d9,
            #0da7d8,
            #06142f
        );
    background-size:400% 400%;
    animation:gradientShift 16s ease infinite;
}

@keyframes gradientShift{
    0%{background-position:0% 50%}
    25%{background-position:50% 100%}
    50%{background-position:100% 50%}
    75%{background-position:50% 0%}
    100%{background-position:0% 50%}
}

.glow{
    position:fixed;
    border-radius:50%;
    filter:blur(75px);
    pointer-events:none;
    z-index:-4;
    opacity:.55;
    animation:floatGlow 11s ease-in-out infinite;
}

.g1{
    width:300px;
    height:300px;
    top:4%;
    left:-70px;
    background:rgba(76,170,255,.33);
}

.g2{
    width:340px;
    height:340px;
    top:20%;
    right:-90px;
    background:rgba(160,95,255,.27);
    animation-delay:2s;
}

.g3{
    width:320px;
    height:320px;
    bottom:-90px;
    left:35%;
    background:rgba(0,215,255,.20);
    animation-delay:4s;
}

@keyframes floatGlow{
    0%,100%{transform:translate(0,0) scale(1)}
    50%{transform:translate(18px,-22px) scale(1.08)}
}

/* =========================================================
   LARGE BACKGROUND MOON
========================================================= */

.background-moon{
    position:fixed;
    width:330px;
    height:330px;
    right:5%;
    top:8%;
    border-radius:50%;
    z-index:-3;
    pointer-events:none;

    background:
        radial-gradient(
            circle at 35% 30%,
            #f4fbff 0%,
            #cce9ff 22%,
            #82c8ff 55%,
            #4b83d5 100%
        );

    box-shadow:
        0 0 30px rgba(145,220,255,.8),
        0 0 80px rgba(79,164,255,.55),
        0 0 160px rgba(53,107,255,.30);

    opacity:.82;
    animation:backgroundMoonFloat 8s ease-in-out infinite;
}

.background-moon::before{
    content:"";
    position:absolute;
    inset:-45px;
    border-radius:50%;
    background:
        radial-gradient(
            circle,
            rgba(109,202,255,.20),
            transparent 65%
        );
    filter:blur(15px);
}

@keyframes backgroundMoonFloat{
    0%,100%{
        transform:translateY(0) rotate(-2deg);
    }
    50%{
        transform:translateY(-18px) rotate(2deg);
    }
}

.moon-crater{
    position:absolute;
    border-radius:50%;
    background:rgba(58,119,186,.16);
    box-shadow:inset 3px 4px 6px rgba(47,91,150,.16);
}

.crater1{width:55px;height:55px;left:55px;top:80px}
.crater2{width:35px;height:35px;right:65px;top:55px}
.crater3{width:75px;height:75px;right:50px;bottom:65px}
.crater4{width:28px;height:28px;left:90px;bottom:55px}

/* =========================================================
   STAR BACKGROUND + CLICK BURSTS
========================================================= */

#bgStars{
    position:fixed;
    inset:0;
    z-index:-2;
    overflow:hidden;
}

.bg-star{
    position:absolute;
    color:#fff;
    text-shadow:0 0 9px #78e1ff;
    cursor:pointer;
    user-select:none;
    animation:
        starFloat ease-in-out infinite,
        twinkle ease-in-out infinite;
}

.bg-star:hover{
    transform:scale(1.4);
}

@keyframes starFloat{
    0%,100%{transform:translate(0,0)}
    50%{transform:translate(7px,-14px)}
}

@keyframes twinkle{
    0%,100%{opacity:.25}
    50%{opacity:1}
}

#effects{
    position:fixed;
    inset:0;
    pointer-events:none;
    z-index:9998;
}

.click-star{
    position:absolute;
    color:#fff;
    text-shadow:0 0 10px #7ae6ff;
    animation:burst 1.4s ease-out forwards;
}

@keyframes burst{
    0%{
        opacity:1;
        transform:translate(0,0) scale(.6);
    }
    35%{
        transform:translate(var(--x),var(--y)) scale(1.1) rotate(120deg);
    }
    100%{
        opacity:0;
        transform:
            translate(
                calc(var(--x)*1.3),
                calc(var(--y) - 80px)
            )
            scale(.2)
            rotate(240deg);
    }
}

/* =========================================================
   SHARED UI
========================================================= */

.panel{
    background:rgba(5,20,49,.85);
    border:2px solid rgba(111,194,255,.4);
    box-shadow:10px 10px 0 rgba(0,0,0,.27);
    backdrop-filter:blur(8px);
    padding:25px;
}

.section{
    width:min(1120px,calc(100% - 34px));
    margin:auto;
    padding:70px 0;
    position:relative;
    z-index:2;
}

.section-title{
    color:var(--cyan);
    letter-spacing:3px;
    font-size:.78rem;
}

h2{
    font-size:clamp(1.7rem,5vw,2.8rem);
}

.btn{
    display:inline-block;
    border:2px solid var(--cyan);
    background:#102e68;
    color:white;
    padding:13px 18px;
    cursor:pointer;
    box-shadow:4px 4px 0 rgba(0,0,0,.3);
    transition:.15s;
    text-decoration:none;
}

.btn:hover{
    transform:translate(-2px,-2px);
    background:#1951aa;
}

.btn.primary{
    background:linear-gradient(135deg,#53afff,#4481ff);
    color:#02132c;
    font-weight:bold;
}

/* =========================================================
   INTRO
========================================================= */

#intro{
    min-height:100vh;
    display:grid;
    place-items:center;
    padding:25px;
    position:relative;
    z-index:5;
}

.intro{
    width:min(720px,100%);
    text-align:center;
}

.intro h1{
    font-size:clamp(2rem,7vw,4.8rem);
    text-shadow:5px 5px rgba(0,0,0,.35);
}

.load{
    height:22px;
    border:2px solid var(--cyan);
    background:#01091b;
    margin:25px 0;
    overflow:hidden;
}

.load>div{
    height:100%;
    width:0;
    background:linear-gradient(90deg,var(--blue),var(--cyan),var(--purple));
    transition:width 2s;
}

/* =========================================================
   HERO
========================================================= */

.hero{
    min-height:95vh;
    display:grid;
    place-items:center;
    padding:60px 22px;
}

.hero-layout{
    width:min(1200px,100%);
    display:grid;
    grid-template-columns:1.05fr .95fr;
    gap:35px;
    align-items:center;
}

.hero-copy{
    background:rgba(5,20,50,.68);
    border:2px solid rgba(124,205,255,.33);
    padding:32px;
    box-shadow:12px 12px rgba(0,0,0,.25);
    backdrop-filter:blur(8px);
}

.badge{
    display:inline-block;
    padding:7px 13px;
    background:#eaf5ff;
    color:#06204c;
    border:2px solid #09214b;
    font-weight:bold;
    transform:rotate(-2deg);
}

.hero h1{
    font-size:clamp(3rem,8vw,6.5rem);
    line-height:.9;
    margin:20px 0;
    text-shadow:6px 6px rgba(0,0,0,.35);
}

.stats{
    display:flex;
    flex-wrap:wrap;
    gap:8px;
    margin-top:20px;
}

.stats span{
    padding:8px 11px;
    border:1px solid rgba(122,206,255,.47);
    background:rgba(4,16,42,.74);
}

/* =========================================================
   HERO MOON / MUSIC PLAYER
========================================================= */

.hero-side{
    min-height:580px;
    position:relative;
    display:flex;
    align-items:center;
    justify-content:center;
}

.orbit{
    position:absolute;
    width:500px;
    height:500px;
}

.moon{
    position:absolute;
    left:50%;
    top:50%;
    transform:translate(-50%,-50%);
    width:145px;
    height:145px;
    display:grid;
    place-items:center;
    border-radius:50%;
    font-size:5rem;
    background:
        radial-gradient(
            circle at 35% 30%,
            #e8f9ff,
            #6bc5ff 45%,
            #3674d8
        );
    box-shadow:
        0 0 40px #53aaff,
        0 0 100px rgba(70,144,255,.53);
    animation:moonPulse 4s ease-in-out infinite;
}

@keyframes moonPulse{
    0%,100%{transform:translate(-50%,-50%) scale(1)}
    50%{transform:translate(-50%,-50%) scale(1.06)}
}

.ring{
    position:absolute;
    left:50%;
    top:50%;
    border-radius:50%;
    border:1px solid rgba(130,215,255,.28);
}

.r1{
    width:310px;
    height:310px;
    margin:-155px;
    animation:spin 15s linear infinite;
}

.r2{
    width:450px;
    height:450px;
    margin:-225px;
    animation:spin2 24s linear infinite;
}

@keyframes spin{
    to{transform:rotate(360deg)}
}

@keyframes spin2{
    to{transform:rotate(-360deg)}
}

.oi{
    position:absolute;
    font-size:2.2rem;
    filter:drop-shadow(0 0 10px rgba(100,210,255,.8));
    animation:bob 3s ease-in-out infinite;
}

@keyframes bob{
    50%{transform:translateY(-12px)}
}

.i1{left:10%;top:17%}
.i2{right:10%;top:12%}
.i3{right:4%;top:50%}
.i4{right:18%;bottom:8%}
.i5{left:14%;bottom:7%}
.i6{left:2%;top:52%}

.music-card{
    position:absolute;
    width:min(330px,90%);
    bottom:-15px;
    padding:20px;
    text-align:center;
    background:rgba(4,17,45,.90);
    border:2px solid rgba(118,208,255,.5);
    box-shadow:9px 9px rgba(0,0,0,.25);
    backdrop-filter:blur(9px);
    z-index:5;
}

.disc{
    width:80px;
    height:80px;
    margin:10px auto;
    border-radius:50%;
    display:grid;
    place-items:center;
    font-size:2.5rem;
    background:linear-gradient(135deg,#197fff,#67d4ff,#735cff);
    animation:spin 8s linear infinite;
    animation-play-state:paused;
}

.music-playing .disc{
    animation-play-state:running;
}

.viz{
    height:55px;
    display:flex;
    align-items:center;
    justify-content:center;
    gap:4px;
    margin:15px 0;
}

.viz span{
    width:6px;
    height:10px;
    background:linear-gradient(#72e8ff,#267cff);
    border-radius:4px;
    animation:eq 1s ease-in-out infinite;
    animation-play-state:paused;
}

.music-playing .viz span{
    animation-play-state:running;
}

.viz span:nth-child(2){animation-delay:.1s}
.viz span:nth-child(3){animation-delay:.2s}
.viz span:nth-child(4){animation-delay:.3s}
.viz span:nth-child(5){animation-delay:.15s}
.viz span:nth-child(6){animation-delay:.25s}
.viz span:nth-child(7){animation-delay:.05s}
.viz span:nth-child(8){animation-delay:.35s}

@keyframes eq{
    50%{height:48px}
}

/* =========================================================
   NAV + SECTIONS
========================================================= */

nav{
    position:sticky;
    top:0;
    z-index:100;
    display:flex;
    justify-content:center;
    gap:5px;
    flex-wrap:wrap;
    background:rgba(2,10,28,.92);
    backdrop-filter:blur(10px);
    padding:11px;
}

nav a{
    color:var(--cyan);
    text-decoration:none;
    padding:7px 10px;
}

.status-grid,.grid,.inventory{
    display:grid;
    grid-template-columns:repeat(4,1fr);
    gap:14px;
}

.inventory{
    grid-template-columns:repeat(3,1fr);
}

.status-card,.item,.choice{
    padding:18px;
    background:rgba(12,42,92,.86);
    border:2px solid rgba(107,190,255,.33);
    box-shadow:6px 6px rgba(0,0,0,.20);
}

.status-card{
    text-align:center;
}

.status-card span{
    font-size:3rem;
}

.choice{
    color:white;
    cursor:pointer;
    text-align:left;
}

.choice:hover,.choice.selected{
    background:#1653a8;
    transform:translateY(-4px);
}

.choice .big{
    font-size:2.3rem;
}

.choice b,.choice small{
    display:block;
    margin-top:8px;
}

.quest-list{
    display:grid;
    gap:10px;
}

.quest-list label{
    padding:12px;
    border:1px solid rgba(100,180,255,.27);
    background:rgba(255,255,255,.035);
}

.button-row{
    display:flex;
    flex-wrap:wrap;
    gap:12px;
    margin-top:25px;
}

.hp{
    height:24px;
    border:2px solid white;
    background:#240d17;
}

.hp>div{
    height:100%;
    width:100%;
    background:linear-gradient(90deg,#ff3b5d,#ff9872);
    transition:.3s;
}

.cat-zone{
    min-height:440px;
    position:relative;
}

.cat{
    position:absolute;
    border:0;
    background:transparent;
    font-size:2.8rem;
    cursor:pointer;
}

.cat.found{
    opacity:.12;
    pointer-events:none;
}

.c1{left:7%;top:13%}
.c2{left:30%;top:65%}
.c3{right:10%;top:20%}
.c4{right:26%;bottom:12%}
.c5{left:55%;top:13%}
.c6{left:12%;bottom:12%}
.c7{right:4%;bottom:25%}

/* =========================================================
   MEDTECH
========================================================= */

.two{
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:20px;
}

.stat{
    margin:16px 0;
}

.bar{
    height:12px;
    background:#020c1e;
    border:1px solid rgba(90,155,225,.47);
}

.fill{
    height:100%;
    background:linear-gradient(90deg,var(--blue),var(--cyan));
}

.labcat{
    text-align:center;
    font-size:6rem;
}

.scope{
    width:min(350px,100%);
    height:350px;
    margin:25px auto;
    border-radius:50%;
    position:relative;
    border:12px solid #163a78;
    background:radial-gradient(circle,#376bc8,#102858 70%);
}

.cell{
    position:absolute;
    width:58px;
    height:58px;
    border-radius:50%;
    border:2px solid var(--cyan);
    background:rgba(255,255,255,.13);
    color:white;
    cursor:pointer;
}

.a{top:15%;left:20%}
.b{top:24%;right:15%}
.c{top:48%;left:43%}
.d{bottom:15%;left:18%}
.e{bottom:17%;right:17%}

.tubes{
    text-align:center;
}

.tube{
    border:0;
    background:transparent;
    font-size:4rem;
    cursor:pointer;
}

.report{
    display:grid;
    grid-template-columns:1fr 1fr;
}

.report span,.report b{
    padding:10px;
    border-bottom:1px dashed rgba(111,180,255,.33);
}

/* =========================================================
   CAKE / TERMINAL / FINAL
========================================================= */

.cake{
    text-align:center;
    font-size:8rem;
}

.cake-area{
    text-align:center;
}

.candle{
    border:0;
    background:transparent;
    font-size:2rem;
    cursor:pointer;
}

.terminal{
    background:#010a12;
    color:#7dffae;
}

.terminal-output{
    height:220px;
    overflow-y:auto;
}

.terminal-input{
    display:flex;
    gap:8px;
    border-top:1px solid rgba(125,255,174,.2);
    padding-top:12px;
}

.terminal-input input{
    flex:1;
    background:transparent;
    border:0;
    outline:0;
    color:#7dffae;
}

.final{
    text-align:center;
}

.final h2{
    font-size:clamp(2.5rem,8vw,5.8rem);
}

.final-stats{
    max-width:600px;
    margin:25px auto;
    display:grid;
    gap:9px;
}

.final-stats div{
    border:1px solid rgba(110,191,255,.33);
    padding:11px;
    background:rgba(255,255,255,.035);
}

/* =========================================================
   WISH LOADING
========================================================= */

.wish-loading-box{
    width:100%;
    max-width:420px;
    margin:20px auto;
}

.wish-progress-track{
    width:100%;
    height:24px;
    border:2px solid #79e7ff;
    background:#020a1c;
    overflow:hidden;
    box-shadow:0 0 15px rgba(80,190,255,.25);
}

#wishProgressBar{
    width:0%;
    height:100%;
    background:
        linear-gradient(
            90deg,
            #238cff,
            #79e7ff,
            #9a79ff
        );
    box-shadow:0 0 15px rgba(121,231,255,.65);
    transition:width .08s linear;
}

#wishPercent{
    margin-top:12px;
    color:#79e7ff;
    font-size:1.2rem;
    font-weight:bold;
}

#wishStatus{
    margin-top:18px;
    min-height:50px;
    color:white;
}

/* =========================================================
   TOAST / MODAL / EFFECTS
========================================================= */

#toast{
    position:fixed;
    top:18px;
    right:18px;
    z-index:10001;
    max-width:340px;
    padding:14px 17px;
    color:#041630;
    background:#eff8ff;
    border:3px solid #287bea;
    box-shadow:7px 7px rgba(0,0,0,.3);
    transform:translateY(-180%);
    transition:.3s;
}

#toast.show{
    transform:translateY(0);
}

#modal{
    position:fixed;
    inset:0;
    z-index:9000;
    display:grid;
    place-items:center;
    padding:20px;
    background:rgba(0,0,0,.78);
}

.modal-card{
    max-width:560px;
    width:100%;
    text-align:center;
    position:relative;
}

.close{
    position:absolute;
    right:10px;
    top:5px;
    border:0;
    background:transparent;
    color:white;
    font-size:2rem;
    cursor:pointer;
}

.confetti{
    position:fixed;
    top:-30px;
    z-index:10000;
    pointer-events:none;
    animation:fall linear forwards;
}

@keyframes fall{
    to{
        transform:translateY(110vh) rotate(720deg);
        opacity:.15;
    }
}

.walkcat{
    position:fixed;
    left:-100px;
    bottom:30px;
    z-index:150;
    font-size:4rem;
    pointer-events:none;
    animation:walk 8s linear forwards;
}

@keyframes walk{
    to{left:110vw}
}

/* =========================================================
   RESPONSIVE
========================================================= */

@media(max-width:900px){
    .hero-layout{
        grid-template-columns:1fr;
    }

    .hero-side{
        min-height:590px;
    }

    .grid,.status-grid,.inventory{
        grid-template-columns:repeat(2,1fr);
    }
}

@media(max-width:700px){
    .background-moon{
        width:210px;
        height:210px;
        right:-50px;
        top:80px;
        opacity:.65;
    }
}

@media(max-width:600px){
    .grid,.status-grid,.inventory,.two{
        grid-template-columns:1fr;
    }

    nav{
        justify-content:flex-start;
        flex-wrap:nowrap;
        overflow-x:auto;
    }

    .hero h1{
        font-size:3.1rem;
    }

    .orbit{
        transform:scale(.78);
    }
}
</style>
</head>

<body>

<div class="animated-gradient-bg"></div>
<div class="glow g1"></div>
<div class="glow g2"></div>
<div class="glow g3"></div>

<div class="background-moon">
    <div class="moon-crater crater1"></div>
    <div class="moon-crater crater2"></div>
    <div class="moon-crater crater3"></div>
    <div class="moon-crater crater4"></div>
</div>

<div id="bgStars"></div>
<div id="effects"></div>
<div id="toast"></div>

<section id="intro">
    <div class="panel intro">
        <p class="section-title">★ SYSTEM BOOT ★</p>

        <h1>
            LOADING<br>
            BIRTHDAY FILE...
        </h1>

        <div class="load">
            <div id="loadingBar"></div>
        </div>

        <p>PLAYER: <b>EDJIE GUANGCO</b></p>
        <p>CLASS: <b>MEDTECH STUDENT</b></p>
        <p>STATUS: <b>BIRTHDAY MODE ACTIVE</b></p>

        <button id="startButton" class="btn primary">
            ▶ START BIRTHDAY QUEST
        </button>
    </div>
</section>

<main id="main" class="hidden">

<section class="hero">
    <div class="hero-layout">

        <div class="hero-copy">
            <span class="badge">PLAYER 01</span>

            <h1>
                HAPPY BIRTHDAY,<br>
                EDJIE GUANGCO!
            </h1>

            <p>
                Another year unlocked.<br>
                Somehow you survived.<br><br>
                Birthday mode has officially been activated.
            </p>

            <div class="stats">
                <span>🎮 Gaming +50</span>
                <span>🐱 Cat Energy +999</span>
                <span>🔵 Blue Mode MAX</span>
                <span>🔬 MedTech XP +100</span>
            </div>
        </div>

        <div class="hero-side">

            <div class="orbit">
                <div class="ring r1"></div>
                <div class="ring r2"></div>

                <div class="moon">🌙</div>

                <span class="oi i1">🐱</span>
                <span class="oi i2">🎮</span>
                <span class="oi i3">⭐</span>
                <span class="oi i4">🔬</span>
                <span class="oi i5">💿</span>
                <span class="oi i6">🎧</span>
            </div>

            <div class="music-card">
                <p class="section-title">NOW PLAYING</p>

                <div class="disc">🎧</div>

                <h3>EDJIE'S BIRTHDAY BGM</h3>

                <p id="musicStatus">
                    Press play to start the vibe.
                </p>

                <div class="viz">
                    <span></span><span></span><span></span><span></span>
                    <span></span><span></span><span></span><span></span>
                </div>

                <button id="musicButton" class="btn primary">
                    ▶ PLAY MUSIC
                </button>
            </div>

        </div>
    </div>
</section>

<nav>
    <a href="#status">STATUS</a>
    <a href="#character">COMPANION</a>
    <a href="#quest">QUEST</a>
    <a href="#cats">CATS</a>
    <a href="#medtech">MEDTECH</a>
    <a href="#cake">CAKE</a>
    <a href="#terminal">TERMINAL</a>
    <a href="#final">FINAL</a>
</nav>

<section class="section" id="status">
    <p class="section-title">BIRTHDAY SIGNAL</p>
    <h2>Current Player Status</h2>

    <div class="status-grid">
        <div class="status-card">
            <span>🎮</span>
            <h3>GAMER</h3>
            <p>Birthday gaming buff activated.</p>
        </div>

        <div class="status-card">
            <span>🐱</span>
            <h3>CAT ENJOYER</h3>
            <p>Cat approval currently at maximum.</p>
        </div>

        <div class="status-card">
            <span>🔵</span>
            <h3>BLUE MODE</h3>
            <p>Excessive blue levels detected.</p>
        </div>

        <div class="status-card">
            <span>🔬</span>
            <h3>MEDTECH</h3>
            <p>Future RMT currently loading.</p>
        </div>
    </div>
</section>

<section class="section" id="character">
    <p class="section-title">CHARACTER SELECT</p>
    <h2>Choose Your Birthday Companion</h2>

    <div class="grid">
        <button class="choice companion" data-name="Sleepy Cat">
            <span class="big">😴🐱</span>
            <b>Sleepy Cat</b>
            <small>Passive Skill: Nap anywhere.</small>
        </button>

        <button class="choice companion" data-name="Gamer Cat">
            <span class="big">🎮🐱</span>
            <b>Gamer Cat</b>
            <small>+50 Focus / -80 Sleep</small>
        </button>

        <button class="choice companion" data-name="Suspicious Cat">
            <span class="big">😼</span>
            <b>Suspicious Cat</b>
            <small>Trusts absolutely nobody.</small>
        </button>

        <button class="choice companion" data-name="Lab Cat">
            <span class="big">🐱🥼</span>
            <b>Lab Cat</b>
            <small>Diagnoses everything as CAT.</small>
        </button>
    </div>

    <p id="companionResult">
        Pick one. Your choice will be judged.
    </p>
</section>

<section class="section" id="quest">
    <p class="section-title">MAIN QUEST</p>
    <h2>Birthday Mission</h2>

    <div class="panel quest-list">
        <label><input type="checkbox"> Eat something actually good.</label>
        <label><input type="checkbox"> Play at least one game.</label>
        <label><input type="checkbox"> Take a break from school stress.</label>
        <label><input type="checkbox"> Laugh at something stupid.</label>
        <label><input type="checkbox"> Find all hidden cats.</label>
        <label><input type="checkbox"> Successfully level up.</label>
    </div>

    <div class="button-row">
        <button id="wishButton" class="btn">🌠 MAKE A WISH</button>
        <button id="giftButton" class="btn">🎁 MYSTERY ITEM</button>
        <button id="catButton" class="btn">🐱 SUSPICIOUS BUTTON</button>
    </div>
</section>

<section class="section">
    <p class="section-title">PLAYER INVENTORY</p>
    <h2>Birthday Inventory</h2>

    <div class="inventory">
        <div class="item">🎂<b>Cake</b><small>Quantity: 1</small></div>
        <div class="item">🎮<b>Games</b><small>Never enough</small></div>
        <div class="item">🐱<b>Cats</b><small>Also never enough</small></div>
        <div class="item">🔵<b>Blue Things</b><small>Maximum</small></div>
        <div class="item">😴<b>Sleep</b><small>Critically low</small></div>
        <div class="item">⭐<b>Luck</b><small>+50</small></div>
    </div>
</section>

<section class="section">
    <div class="panel">
        <p class="section-title">⚠ MINI BOSS</p>
        <h2>RESPONSIBILITIES</h2>

        <div class="hp">
            <div id="bossHP"></div>
        </div>

        <p id="bossText">HP: 100%</p>

        <button id="attackButton" class="btn">
            ⚔ ATTACK
        </button>
    </div>
</section>

<section class="section" id="cats">
    <p class="section-title">SIDE QUEST</p>
    <h2>Find All 7 Cats</h2>

    <div class="panel cat-zone">
        <p>They're definitely not hiding very well.</p>

        <button class="cat c1">🐱</button>
        <button class="cat c2">🐈</button>
        <button class="cat c3">😼</button>
        <button class="cat c4">🐈‍⬛</button>
        <button class="cat c5">😺</button>
        <button class="cat c6">🐱</button>
        <button class="cat c7">🐈</button>

        <p>
            CATS FOUND:
            <b id="catCounter">0</b> / 7
        </p>
    </div>
</section>

<section class="section">
    <p class="section-title">CHOOSE YOUR BUFF</p>
    <h2>One Bonus For This Year</h2>

    <div class="grid">
        <button class="choice buff" data-buff="+50 Luck">
            ⭐<b>+50 Luck</b>
        </button>

        <button class="choice buff" data-buff="+50 Money">
            💰<b>+50 Money</b>
        </button>

        <button class="choice buff" data-buff="+50 Gaming Skill">
            🎮<b>+50 Gaming Skill</b>
        </button>

        <button class="choice buff" data-buff="+50 Sleep">
            😴<b>+50 Sleep</b>
        </button>
    </div>

    <p id="buffResult">
        Choose wisely. This is extremely scientific.
    </p>
</section>

<section class="section" id="medtech">
    <p class="section-title">MEDTECH EXPANSION PACK</p>
    <h2>Survive MedTech</h2>

    <div class="two">

        <div class="panel">
            <p>PLAYER: <b>EDJIE GUANGCO</b></p>
            <p>CLASS: <b>MEDTECH STUDENT</b></p>

            <div class="stat">
                🔬 Laboratory Skill
                <div class="bar">
                    <div class="fill" style="width:78%"></div>
                </div>
            </div>

            <div class="stat">
                🎮 Gaming
                <div class="bar">
                    <div class="fill" style="width:95%"></div>
                </div>
            </div>

            <div class="stat">
                🐱 Cat Appreciation
                <div class="bar">
                    <div class="fill" style="width:100%"></div>
                </div>
            </div>

            <div class="stat">
                🔵 Blue Energy
                <div class="bar">
                    <div class="fill" style="width:100%"></div>
                </div>
            </div>

            <div class="stat">
                😴 Sleep
                <div class="bar">
                    <div class="fill" style="width:20%"></div>
                </div>
            </div>
        </div>

        <div class="panel">
            <p class="section-title">LAB CAT REPORT</p>

            <div class="labcat">🐱🥼</div>

            <p>"Specimen received."</p>
            <p>"Specimen is Edjie."</p>
            <p>"Diagnosis: Birthday."</p>

            <button id="labButton" class="btn">
                🔬 VIEW RESULTS
            </button>
        </div>

    </div>

    <br>

    <div class="two">

        <div class="panel">
            <p class="section-title">MICROSCOPE MODE</p>
            <h3>Find the suspicious cell.</h3>

            <div class="scope">
                <button class="cell a">◉</button>
                <button class="cell b">◉</button>
                <button class="cell c cat-cell">🐱</button>
                <button class="cell d">◉</button>
                <button class="cell e">◉</button>
            </div>

            <p id="microResult">
                RESULT: Waiting...
            </p>
        </div>

        <div class="panel tubes">
            <p class="section-title">TEST TUBE MINI GAME</p>
            <h3>Choose one totally scientific tube.</h3>

            <button class="tube" data-tube="Birthday Energy">🧪</button>
            <button class="tube" data-tube="Gaming Skill">🧪</button>
            <button class="tube" data-tube="Good Luck">🧪</button>
            <button class="tube" data-tube="Unknown">🧪</button>

            <p id="tubeResult">
                Select a tube.
            </p>
        </div>

    </div>

    <br>

    <div class="panel">
        <p class="section-title">ANNUAL BIRTHDAY SCREENING</p>

        <div class="report">
            <span>Happiness</span><b>↑ HIGH</b>
            <span>Gaming Desire</span><b>↑ HIGH</b>
            <span>Cat Appreciation</span><b>↑ EXTREMELY HIGH</b>
            <span>Blue Preference</span><b>↑ MAXIMUM</b>
            <span>Stress</span><b>Hopefully ↓ LOW</b>
            <span>Birthday Cake</span><b>INSUFFICIENT</b>
            <span>Sleep</span><b>PLEASE RECHECK</b>
        </div>

        <p>
            <b>FINAL INTERPRETATION:</b>
            Patient has successfully leveled up another year.
        </p>
    </div>
</section>

<section class="section" id="cake">
    <p class="section-title">BONUS ROUND</p>
    <h2>Birthday Cake</h2>

    <div class="panel cake-area">
        <div class="cake">🎂</div>

        <p>Click every candle.</p>

        <button class="candle">🔥</button>
        <button class="candle">🔥</button>
        <button class="candle">🔥</button>
        <button class="candle">🔥</button>

        <p id="cakeResult">
            Candles remaining: 4
        </p>
    </div>
</section>

<section class="section" id="terminal">
    <p class="section-title">OLD COMPUTER TERMINAL</p>
    <h2>Type A Command</h2>

    <div class="panel terminal">

        <div id="terminalOutput" class="terminal-output">
            <p>EDJIE_OS v20.26</p>
            <p>Type HELP to see commands.</p>
        </div>

        <div class="terminal-input">
            <span>&gt;</span>
            <input id="terminalInput" placeholder="Enter command">
        </div>

    </div>
</section>

<section class="section final" id="final">

    <div class="panel">

        <p class="section-title">⚠ FINAL LEVEL</p>

        <h2>
            Ready to finish the quest?
        </h2>

        <button id="finalButton" class="btn primary">
            CONTINUE?
        </button>

        <div id="finalMessage" class="hidden">

            <h2>
                HAPPY BIRTHDAY,<br>
                EDJIE GUANGCO.
            </h2>

            <p>
                Just wanted to make something fun for you instead of sending a plain birthday message.
            </p>

            <p>
                Hope you enjoy your day, get to do the things you like, eat something good, play some games, and have a great year ahead.
            </p>

            <p>
                More wins, more random good memories, more cats, and hopefully less stress.
            </p>

            <div class="final-stats">
                <div>🎮 PLAYER LEVEL +1</div>
                <div>🐱 CAT APPROVAL MAX</div>
                <div>🔵 BLUE ENERGY MAX</div>
                <div>🔬 FUTURE RMT: IN PROGRESS</div>
            </div>

            <h3>SAVE COMPLETE.</h3>

            <p>
                See you next level. 🎮🐱🔵
            </p>

        </div>

    </div>

</section>

</main>

<div id="modal" class="hidden">
    <div class="panel modal-card">

        <button id="closeModal" class="close">
            ×
        </button>

        <div id="modalContent"></div>

    </div>
</div>

<script>

const $ = s => document.querySelector(s);
const $$ = s => [...document.querySelectorAll(s)];

/* =========================================================
   TOAST + MODAL
========================================================= */

let toastTimer;

function toast(msg){
    clearTimeout(toastTimer);

    $("#toast").innerHTML = msg;
    $("#toast").classList.add("show");

    toastTimer = setTimeout(() => {
        $("#toast").classList.remove("show");
    },2800);
}

function modal(html){
    $("#modalContent").innerHTML = html;
    $("#modal").classList.remove("hidden");
}

$("#closeModal").onclick = () => {
    $("#modal").classList.add("hidden");
};

$("#modal").onclick = e => {
    if(e.target.id === "modal"){
        $("#modal").classList.add("hidden");
    }
};

/* =========================================================
   INTRO
========================================================= */

window.onload = () => {
    setTimeout(() => {
        $("#loadingBar").style.width = "100%";
    },300);
};

$("#startButton").onclick = () => {
    $("#intro").classList.add("hidden");
    $("#main").classList.remove("hidden");

    toast(
        "🏆 BIRTHDAY QUEST STARTED"
    );

    setTimeout(walkCat,2200);
};

/* =========================================================
   MUSIC
========================================================= */

let music = null;
let fade = null;

$("#musicButton").onclick = function(){

    if(!music){
        music = new Audio("/static/audio/bgm.mp3");
        music.loop = true;
        music.volume = 0;
    }

    if(music.paused){

        music.play()
        .then(() => {

            clearInterval(fade);

            fade = setInterval(() => {

                if(music.volume < .35){
                    music.volume =
                        Math.min(
                            .35,
                            music.volume + .02
                        );
                }
                else{
                    clearInterval(fade);
                }

            },80);

            this.textContent =
                "⏸ PAUSE MUSIC";

            $("#musicStatus").textContent =
                "Birthday soundtrack currently playing.";

            $(".music-card")
                .classList
                .add("music-playing");

            toast(
                "🎧 BIRTHDAY BGM STARTED"
            );

        })
        .catch(() => {
            toast(
                "⚠ Put bgm.mp3 inside static/audio/"
            );
        });

    }
    else{

        music.pause();

        this.textContent =
            "▶ PLAY MUSIC";

        $("#musicStatus").textContent =
            "Music paused.";

        $(".music-card")
            .classList
            .remove("music-playing");
    }
};

/* =========================================================
   STARS
========================================================= */

function stars(){

    const layer = $("#bgStars");

    const icons = [
        "✦","✧","★","☆","⋆"
    ];

    for(let i=0;i<70;i++){

        let star =
            document.createElement(
                "span"
            );

        star.className =
            "bg-star";

        star.textContent =
            icons[
                Math.floor(
                    Math.random()
                    *
                    icons.length
                )
            ];

        star.style.left =
            Math.random()*100
            + "%";

        star.style.top =
            Math.random()*100
            + "%";

        star.style.fontSize =
            (
                8
                +
                Math.random()*18
            )
            + "px";

        star.style.animationDuration =
            (
                4
                +
                Math.random()*6
            )
            + "s,"
            +
            (
                2
                +
                Math.random()*3
            )
            + "s";

        star.onclick = e => {

            e.stopPropagation();

            let r =
                star.getBoundingClientRect();

            burst(
                r.left + r.width/2,
                r.top + r.height/2
            );

            star.style.left =
                Math.random()*100
                + "%";

            star.style.top =
                Math.random()*100
                + "%";

            toast(
                "⭐ STAR COLLECTED"
            );
        };

        layer.appendChild(star);
    }
}

stars();

function burst(x,y){

    const container =
        $("#effects");

    const icons =
        ["✦","★","✧","☆","⋆"];

    for(let i=0;i<10;i++){

        let star =
            document.createElement(
                "span"
            );

        star.className =
            "click-star";

        star.textContent =
            icons[
                Math.floor(
                    Math.random()
                    *
                    icons.length
                )
            ];

        star.style.left =
            x + "px";

        star.style.top =
            y + "px";

        star.style.setProperty(
            "--x",
            (
                Math.random()*120
                -
                60
            )
            + "px"
        );

        star.style.setProperty(
            "--y",
            (
                Math.random()*60
                -
                30
            )
            + "px"
        );

        container.appendChild(star);

        setTimeout(
            () => star.remove(),
            1400
        );
    }
}

document.addEventListener(
    "click",
    e => {

        if(
            !e.target.closest(
                "button,a,input"
            )
        ){
            burst(
                e.clientX,
                e.clientY
            );
        }
    }
);

/* =========================================================
   COMPANION
========================================================= */

$$(".companion").forEach(
    b => {

        b.onclick = () => {

            $$(".companion")
            .forEach(
                x =>
                    x.classList
                    .remove("selected")
            );

            b.classList.add(
                "selected"
            );

            $("#companionResult")
                .innerHTML =

                "<b>"
                +
                b.dataset.name
                +
                "</b> selected."
                +
                "<br>"
                +
                "Your companion will now judge every decision you make.";

            toast(
                "🐱 COMPANION ACQUIRED"
            );
        };
    }
);

/* =========================================================
   REAL WISH LOADING 0 -> 100
========================================================= */

$("#wishButton").onclick = () => {

    modal(`
        <h2>
            🌠 TRANSMITTING WISH...
        </h2>

        <p>
            Please wait while your wish travels through space.
        </p>

        <div class="wish-loading-box">

            <div class="wish-progress-track">
                <div id="wishProgressBar"></div>
            </div>

            <div id="wishPercent">
                0%
            </div>

            <div id="wishStatus">
                Preparing wish...
            </div>

        </div>
    `);

    const bar =
        document.getElementById(
            "wishProgressBar"
        );

    const percent =
        document.getElementById(
            "wishPercent"
        );

    const status =
        document.getElementById(
            "wishStatus"
        );

    let progress = 0;

    const loading =
        setInterval(() => {

            progress += 1;

            if(progress > 100){
                progress = 100;
            }

            bar.style.width =
                progress + "%";

            percent.textContent =
                progress + "%";

            if(progress < 20){

                status.textContent =
                    "Preparing wish...";

            }
            else if(progress < 40){

                status.textContent =
                    "Locating nearest star...";

            }
            else if(progress < 60){

                status.textContent =
                    "Sending birthday signal...";

            }
            else if(progress < 80){

                status.textContent =
                    "Passing the moon... 🌙";

            }
            else if(progress < 100){

                status.textContent =
                    "Almost there...";

            }

            if(progress === 100){

                clearInterval(
                    loading
                );

                status.innerHTML = `

                    <h3>
                        ⭐ WISH SUCCESSFULLY SENT.
                    </h3>

                    <p>
                        Destination:
                        Somewhere in the universe.
                    </p>

                    <p>
                        Delivery status:
                        Probably successful.
                    </p>

                `;

                confetti(
                    [
                        "⭐",
                        "✦",
                        "🔵",
                        "✨",
                        "🌙"
                    ],
                    70
                );

                toast(
                    "🌠 WISH TRANSMISSION COMPLETE"
                );
            }

        },35);
};

/* =========================================================
   MYSTERY GIFT + CAT BUTTON
========================================================= */

$("#giftButton").onclick = () => {

    modal(`
        <h2>
            🎁 RARE ITEM ACQUIRED
        </h2>

        <h3>
            ONE BIRTHDAY WISH
        </h3>

        <p>
            ⭐ Better luck
            <br>
            🎮 Better games
            <br>
            🐱 More cats
            <br>
            😂 More laughs
            <br>
            😴 Better sleep
            <br>
            🔵 Excessive amounts of blue
        </p>
    `);
};

$("#catButton").onclick = () => {

    toast(
        "Nothing happened."
    );

    setTimeout(
        () => {

            walkCat();

            toast(
                "🐱 Never mind."
            );

        },
        1400
    );
};

/* =========================================================
   BOSS
========================================================= */

let hp = 100;

$("#attackButton").onclick =
function(){

    hp = Math.max(
        0,
        hp - 25
    );

    $("#bossHP").style.width =
        hp + "%";

    $("#bossText").textContent =
        "HP: "
        +
        hp
        +
        "%";

    if(!hp){

        this.disabled =
            true;

        this.textContent =
            "BOSS DEFEATED";

        toast(
            "🏆 BOSS DEFEATED"
        );
    }
};

/* =========================================================
   CAT HUNT
========================================================= */

let found = 0;

const msgs = [
    "You found one.",
    "Nice.",
    "You are actually doing this?",
    "Do not question the number of cats.",
    "Almost there.",
    "One left...",
    "CAT COLLECTION COMPLETE."
];

$$(".cat").forEach(
    (cat,index) => {

        cat.onclick = () => {

            if(
                cat.classList
                .contains("found")
            ){
                return;
            }

            cat.classList.add(
                "found"
            );

            $("#catCounter")
                .textContent =
                ++found;

            toast(
                "🐱 "
                +
                msgs[index]
            );

            if(found === 7){

                modal(`
                    <h2>
                        🏆 ACHIEVEMENT UNLOCKED
                    </h2>

                    <h3>
                        PROFESSIONAL CAT FINDER
                    </h3>

                    <p>
                        Reward:
                        +999 Cat Respect
                    </p>
                `);

                confetti(
                    [
                        "🐱",
                        "🔵",
                        "⭐"
                    ],
                    70
                );
            }
        };
    }
);

/* =========================================================
   BUFF
========================================================= */

$$(".buff").forEach(
    b => {

        b.onclick = () => {

            $$(".buff")
            .forEach(
                x =>
                    x.classList
                    .remove("selected")
            );

            b.classList.add(
                "selected"
            );

            $("#buffResult")
            .innerHTML =

                "<b>"
                +
                b.dataset.buff
                +
                "</b> applied."
                +
                "<br>"
                +
                "Effect lasts approximately one year."
                +
                "<br>"
                +
                "Probably.";

            toast(
                "⭐ BUFF APPLIED"
            );
        };
    }
);

/* =========================================================
   MEDTECH
========================================================= */

$("#labButton").onclick = () => {

    modal(`
        <h2>
            🔬 LAB RESULTS READY
        </h2>

        <p>
            Gaming:
            <b>HIGH</b>
        </p>

        <p>
            Cat Appreciation:
            <b>EXTREMELY HIGH</b>
        </p>

        <p>
            Blue Levels:
            <b>MAXIMUM</b>
        </p>

        <p>
            Birthday Energy:
            <b>HIGH</b>
        </p>

        <h3>
            FINAL RESULT
        </h3>

        <p>
            NORMAL EDJIE BEHAVIOR.
        </p>
    `);
};

$$(".cell").forEach(
    cell => {

        cell.onclick = () => {

            $("#microResult")
            .innerHTML =

                cell
                .classList
                .contains(
                    "cat-cell"
                )

                ?

                "DIAGNOSIS: <b>CAT.</b><br>RESULT: POSITIVE."

                :

                "Normal-looking cell. Keep searching...";
        };
    }
);

$$(".tube").forEach(
    tube => {

        tube.onclick = () => {

            $("#tubeResult")
            .innerHTML =

                tube.dataset.tube
                === "Unknown"

                ?

                "⚠ WARNING"
                +
                "<br><br>"
                +
                "Probably shouldn't have touched that."
                +
                "<br><br>"
                +
                "🐱"
                +
                "<br>"
                +
                "Never mind. It was a cat."

                :

                "<b>"
                +
                tube.dataset.tube
                +
                "</b> acquired."
                +
                "<br>"
                +
                "Totally scientific.";
        };
    }
);

/* =========================================================
   CAKE
========================================================= */

let candles = 4;

$$(".candle").forEach(
    candle => {

        candle.onclick = () => {

            if(
                candle.textContent.trim()
                === "💨"
            ){
                return;
            }

            candle.textContent =
                "💨";

            $("#cakeResult")
                .textContent =

                "Candles remaining: "
                +
                (--candles);

            if(!candles){

                $("#cakeResult")
                .innerHTML =

                    "<b>BONUS ROUND COMPLETE</b>"
                    +
                    "<br>"
                    +
                    "+1 YEAR"
                    +
                    "<br>"
                    +
                    "+10 WISDOM"
                    +
                    "<br>"
                    +
                    "+20 LUCK"
                    +
                    "<br>"
                    +
                    "+50 GAMING SKILL"
                    +
                    "<br>"
                    +
                    "+999 CAT ENERGY";

                confetti(
                    [
                        "🔵",
                        "⭐",
                        "🐱",
                        "🎮",
                        "✨"
                    ],
                    90
                );
            }
        };
    }
);

/* =========================================================
   TERMINAL
========================================================= */

const responses = {

    HELP:
        "Commands: HELP, CAT, MOON, GAME, BIRTHDAY, EDJIE, MEDTECH, SECRET",

    CAT:
        "Cats detected. System functioning normally.",

    MOON:
        "Moon status: still cool.",

    GAME:
        "Current objective: enjoy birthday.",

    BIRTHDAY:
        "Birthday protocol successfully activated.",

    EDJIE:
        "Player identified: Edjie Guangco. Class: MedTech Student.",

    MEDTECH:
        "Future RMT detected. Loading laboratory survival skills...",

    SECRET:
        "You found absolutely nothing..."
};

$("#terminalInput").onkeydown =
e => {

    if(
        e.key !== "Enter"
    ){
        return;
    }

    let cmd =
        e.target
        .value
        .trim()
        .toUpperCase();

    if(!cmd){
        return;
    }

    let output =
        $("#terminalOutput");

    output.innerHTML +=
        "<p>&gt; "
        +
        cmd
        +
        "</p>"
        +
        "<p>"
        +
        (
            responses[cmd]
            ||
            "Unknown command. Type HELP."
        )
        +
        "</p>";

    if(
        cmd === "SECRET"
    ){

        setTimeout(
            () => {

                output.innerHTML +=
                    "<p>🐱 GIANT CAT EVENT TRIGGERED.</p>";

                walkCat();

            },
            800
        );
    }

    e.target.value =
        "";

    output.scrollTop =
        output.scrollHeight;
};

/* =========================================================
   FINAL
========================================================= */

$("#finalButton").onclick =
function(){

    this.classList.add(
        "hidden"
    );

    $("#finalMessage")
        .classList
        .remove(
            "hidden"
        );

    confetti(
        [
            "🔵",
            "⭐",
            "🐱",
            "🎮",
            "🔬",
            "✨"
        ],
        160
    );

    toast(
        "🏆 QUEST COMPLETE"
        +
        "<br>"
        +
        "<b>HAPPY BIRTHDAY EDJIE!</b>"
    );

    setTimeout(
        walkCat,
        900
    );
};

/* =========================================================
   WALKING CAT + CONFETTI
========================================================= */

function walkCat(){

    let cat =
        document
        .createElement(
            "div"
        );

    cat.className =
        "walkcat";

    cat.textContent =
        "🐈";

    document.body
        .appendChild(cat);

    setTimeout(
        () => cat.remove(),
        8200
    );
}

function confetti(
    symbols,
    amount
){

    for(
        let i=0;
        i<amount;
        i++
    ){

        let piece =
            document
            .createElement(
                "span"
            );

        piece.className =
            "confetti";

        piece.textContent =
            symbols[
                Math.floor(
                    Math.random()
                    *
                    symbols.length
                )
            ];

        piece.style.left =
            Math.random()*100
            +
            "vw";

        piece.style.fontSize =
            (
                13
                +
                Math.random()*22
            )
            +
            "px";

        piece.style.animationDuration =
            (
                2
                +
                Math.random()*3
            )
            +
            "s";

        document.body
            .appendChild(piece);

        setTimeout(
            () => piece.remove(),
            6000
        );
    }
}

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
