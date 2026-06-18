from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Animation Library — Unlimited Motion</title>
<link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/animate.css/4.1.1/animate.min.css">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.css">
<script src="https://cdnjs.cloudflare.com/ajax/libs/aos/2.3.4/aos.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/particles.js/2.0.0/particles.min.js"></script>
<style>
:root {
  --violet: #6C63FF;
  --purple: #7F5AF0;
  --cyan: #00E5FF;
  --green: #00FFA3;
  --pink: #FF4ECD;
  --yellow: #FFD93D;
  --dark: #0a0a0f;
  --dark2: #111118;
  --dark3: #1a1a2e;
  --glass: rgba(255,255,255,0.05);
  --glass-border: rgba(255,255,255,0.1);
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
body{font-family:'Poppins',sans-serif;background:var(--dark);color:#fff;overflow-x:hidden;cursor:none}

/* ── SCROLLBAR ── */
::-webkit-scrollbar{width:6px}
::-webkit-scrollbar-track{background:var(--dark)}
::-webkit-scrollbar-thumb{background:linear-gradient(var(--violet),var(--pink));border-radius:3px}

/* ── CURSOR ── */
#cursor{position:fixed;width:12px;height:12px;background:var(--cyan);border-radius:50%;pointer-events:none;z-index:9999;transform:translate(-50%,-50%);transition:transform .1s,width .2s,height .2s,background .2s;mix-blend-mode:screen}
#cursor-follower{position:fixed;width:36px;height:36px;border:2px solid rgba(108,99,255,.5);border-radius:50%;pointer-events:none;z-index:9998;transform:translate(-50%,-50%);transition:transform .08s,left .12s ease,top .12s ease}

/* ── LOADING SCREEN ── */
#loading{position:fixed;inset:0;background:var(--dark);z-index:99999;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:20px;transition:opacity .6s,visibility .6s}
#loading.hidden{opacity:0;visibility:hidden;pointer-events:none}
.load-logo{font-size:2rem;font-weight:800;background:linear-gradient(135deg,var(--violet),var(--cyan),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;animation:pulse 1.2s infinite}
.load-bar-wrap{width:200px;height:3px;background:rgba(255,255,255,.1);border-radius:3px;overflow:hidden}
.load-bar{height:100%;width:0;background:linear-gradient(90deg,var(--violet),var(--cyan),var(--pink));border-radius:3px;animation:loadAnim 1.8s ease forwards}
@keyframes loadAnim{to{width:100%}}

/* ── SCROLL PROGRESS ── */
#scroll-progress{position:fixed;top:0;left:0;height:3px;background:linear-gradient(90deg,var(--violet),var(--cyan),var(--pink));z-index:9990;transition:width .1s}

/* ── BACK TO TOP ── */
#back-top{position:fixed;bottom:90px;right:24px;width:44px;height:44px;border-radius:12px;background:linear-gradient(135deg,var(--violet),var(--pink));border:none;color:#fff;font-size:1.1rem;cursor:pointer;z-index:800;display:flex;align-items:center;justify-content:center;opacity:0;transform:translateY(20px);transition:opacity .3s,transform .3s;box-shadow:0 0 20px rgba(108,99,255,.5)}
#back-top.visible{opacity:1;transform:translateY(0)}
#back-top:hover{transform:translateY(-4px) scale(1.05)}

/* ── CHATBOT BTN ── */
#chatbot-btn{position:fixed;bottom:24px;right:24px;width:52px;height:52px;border-radius:50%;background:linear-gradient(135deg,var(--cyan),var(--green));border:none;color:#000;font-size:1.3rem;cursor:none;z-index:800;display:flex;align-items:center;justify-content:center;box-shadow:0 0 25px rgba(0,229,255,.5);animation:floatY 3s ease-in-out infinite}
#chatbot-btn:hover{transform:scale(1.12)}

/* ── DARK MODE TOGGLE ── */
#dm-toggle{position:fixed;top:80px;right:20px;z-index:900;width:44px;height:44px;border-radius:12px;background:var(--glass);border:1px solid var(--glass-border);color:#fff;font-size:1.1rem;cursor:none;display:flex;align-items:center;justify-content:center;backdrop-filter:blur(10px);transition:.3s}
#dm-toggle:hover{background:rgba(255,255,255,.1)}
body.light-mode{--dark:#f0f0f8;--dark2:#e4e4f0;--dark3:#d8d8ee;color:#111}
body.light-mode .nav{background:rgba(240,240,248,.85)}

/* ── PARTICLES ── */
#particles-js{position:fixed;inset:0;z-index:0;pointer-events:none}

/* ── BG BLOBS ── */
.blob{position:fixed;border-radius:50%;filter:blur(80px);opacity:.18;pointer-events:none;z-index:1;animation:blobMove 15s ease-in-out infinite alternate}
.blob1{width:500px;height:500px;background:var(--violet);top:-150px;left:-150px;animation-delay:0s}
.blob2{width:400px;height:400px;background:var(--pink);top:30%;right:-100px;animation-delay:-5s}
.blob3{width:350px;height:350px;background:var(--cyan);bottom:-100px;left:30%;animation-delay:-10s}
@keyframes blobMove{0%{transform:translate(0,0) scale(1)}100%{transform:translate(40px,40px) scale(1.1)}}

/* ── NAV ── */
.nav{position:fixed;top:0;width:100%;z-index:890;padding:18px 5%;display:flex;align-items:center;justify-content:space-between;background:rgba(10,10,15,.8);backdrop-filter:blur(20px);border-bottom:1px solid rgba(255,255,255,.06);transition:all .3s}
.nav-logo{font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,var(--violet),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-decoration:none}
.nav-links{display:flex;gap:32px;list-style:none}
.nav-links a{color:rgba(255,255,255,.7);text-decoration:none;font-size:.9rem;font-weight:500;transition:.3s;position:relative}
.nav-links a::after{content:'';position:absolute;bottom:-4px;left:0;width:0;height:2px;background:linear-gradient(90deg,var(--violet),var(--cyan));transition:.3s;border-radius:2px}
.nav-links a:hover{color:#fff}
.nav-links a:hover::after{width:100%}
.nav-cta{padding:9px 22px;border-radius:10px;background:linear-gradient(135deg,var(--violet),var(--purple));color:#fff;text-decoration:none;font-size:.85rem;font-weight:600;transition:.3s;border:none;cursor:none;box-shadow:0 0 20px rgba(108,99,255,.4)}
.nav-cta:hover{transform:translateY(-2px);box-shadow:0 0 30px rgba(108,99,255,.6)}
.hamburger{display:none;flex-direction:column;gap:5px;cursor:none;z-index:1000}
.hamburger span{display:block;width:24px;height:2px;background:#fff;border-radius:2px;transition:.4s}
.hamburger.open span:nth-child(1){transform:rotate(45deg) translate(5px,5px)}
.hamburger.open span:nth-child(2){opacity:0}
.hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(5px,-5px)}
.mobile-menu{position:fixed;inset:0;background:rgba(10,10,15,.97);backdrop-filter:blur(20px);z-index:880;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:32px;transform:translateX(100%);transition:transform .5s cubic-bezier(.77,0,.18,1)}
.mobile-menu.open{transform:translateX(0)}
.mobile-menu a{color:#fff;text-decoration:none;font-size:1.8rem;font-weight:700;transition:.3s}
.mobile-menu a:hover{background:linear-gradient(135deg,var(--violet),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent}

/* ── HERO ── */
.hero{position:relative;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:120px 5% 80px;overflow:hidden;z-index:2}
.hero-badge{display:inline-flex;align-items:center;gap:8px;padding:7px 16px;border-radius:50px;background:rgba(108,99,255,.15);border:1px solid rgba(108,99,255,.3);color:var(--violet);font-size:.8rem;font-weight:600;margin-bottom:28px;animation:fadeSlideUp .8s ease both}
.hero-badge .dot{width:8px;height:8px;border-radius:50%;background:var(--green);animation:pulse 1.5s infinite}
.hero h1{font-size:clamp(2.4rem,6vw,5.5rem);font-weight:900;line-height:1.1;margin-bottom:24px;animation:fadeSlideUp .9s ease .1s both}
.hero h1 .grad{background:linear-gradient(135deg,var(--violet),var(--cyan),var(--pink));-webkit-background-clip:text;-webkit-text-fill-color:transparent;display:block}
.hero-subtitle{font-size:clamp(1rem,2vw,1.25rem);color:rgba(255,255,255,.6);max-width:580px;margin:0 auto 40px;font-weight:400;animation:fadeSlideUp 1s ease .2s both}
.hero-btns{display:flex;gap:16px;justify-content:center;flex-wrap:wrap;animation:fadeSlideUp 1s ease .3s both}
.btn-primary{padding:14px 34px;border-radius:12px;background:linear-gradient(135deg,var(--violet),var(--purple));color:#fff;text-decoration:none;font-weight:600;font-size:1rem;border:none;cursor:none;transition:.3s;box-shadow:0 0 30px rgba(108,99,255,.45);position:relative;overflow:hidden}
.btn-primary::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,var(--cyan),var(--green));opacity:0;transition:.4s}
.btn-primary:hover::before{opacity:1}
.btn-primary:hover{transform:translateY(-3px);box-shadow:0 0 50px rgba(0,229,255,.4)}
.btn-primary span{position:relative;z-index:1}
.btn-outline{padding:14px 34px;border-radius:12px;background:transparent;color:#fff;text-decoration:none;font-weight:600;font-size:1rem;border:2px solid rgba(255,255,255,.2);cursor:none;transition:.3s;backdrop-filter:blur(10px)}
.btn-outline:hover{border-color:var(--violet);background:rgba(108,99,255,.1);transform:translateY(-3px)}
.hero-glow{position:absolute;width:700px;height:700px;border-radius:50%;background:radial-gradient(circle,rgba(108,99,255,.15) 0%,transparent 70%);top:50%;left:50%;transform:translate(-50%,-50%);pointer-events:none;animation:glowPulse 4s ease-in-out infinite}
@keyframes glowPulse{0%,100%{opacity:.8;transform:translate(-50%,-50%) scale(1)}50%{opacity:1;transform:translate(-50%,-50%) scale(1.08)}}
.hero-scroll{position:absolute;bottom:30px;left:50%;transform:translateX(-50%);display:flex;flex-direction:column;align-items:center;gap:8px;color:rgba(255,255,255,.4);font-size:.75rem;animation:fadeSlideUp 1s ease .6s both}
.scroll-line{width:1px;height:50px;background:linear-gradient(to bottom,transparent,var(--violet));animation:scrollLine 2s ease-in-out infinite}
@keyframes scrollLine{0%,100%{opacity:.4;transform:scaleY(1)}50%{opacity:1;transform:scaleY(1.2)}}

/* ── TYPING ── */
.typing-wrap{display:inline-block;position:relative}
.typing-cursor{display:inline-block;width:3px;height:.9em;background:var(--cyan);animation:blink .75s step-end infinite;vertical-align:text-bottom;margin-left:4px;border-radius:2px}
@keyframes blink{0%,100%{opacity:1}50%{opacity:0}}

/* ── SECTIONS ── */
section{position:relative;z-index:2;padding:100px 5%}
.section-label{font-size:.78rem;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:var(--violet);margin-bottom:12px}
.section-title{font-size:clamp(1.8rem,4vw,3rem);font-weight:800;line-height:1.2;margin-bottom:16px}
.section-sub{color:rgba(255,255,255,.55);font-size:1.05rem;max-width:540px}
.text-center{text-align:center}
.text-center .section-sub{margin:0 auto}

/* ── FEATURES ── */
.features-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:60px}
.feat-card{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:32px 28px;backdrop-filter:blur(20px);transition:.4s;position:relative;overflow:hidden;cursor:none}
.feat-card::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(108,99,255,.1),transparent);opacity:0;transition:.4s;border-radius:20px}
.feat-card:hover{transform:translateY(-8px) scale(1.02);border-color:var(--violet);box-shadow:0 20px 60px rgba(108,99,255,.25)}
.feat-card:hover::before{opacity:1}
.feat-icon{width:56px;height:56px;border-radius:16px;display:flex;align-items:center;justify-content:center;font-size:1.5rem;margin-bottom:20px;position:relative}
.feat-icon.c1{background:linear-gradient(135deg,rgba(108,99,255,.3),rgba(108,99,255,.05));color:var(--violet);box-shadow:0 0 20px rgba(108,99,255,.2)}
.feat-icon.c2{background:linear-gradient(135deg,rgba(0,229,255,.3),rgba(0,229,255,.05));color:var(--cyan);box-shadow:0 0 20px rgba(0,229,255,.2)}
.feat-icon.c3{background:linear-gradient(135deg,rgba(0,255,163,.3),rgba(0,255,163,.05));color:var(--green);box-shadow:0 0 20px rgba(0,255,163,.2)}
.feat-icon.c4{background:linear-gradient(135deg,rgba(255,78,205,.3),rgba(255,78,205,.05));color:var(--pink);box-shadow:0 0 20px rgba(255,78,205,.2)}
.feat-icon.c5{background:linear-gradient(135deg,rgba(255,217,61,.3),rgba(255,217,61,.05));color:var(--yellow);box-shadow:0 0 20px rgba(255,217,61,.2)}
.feat-icon.c6{background:linear-gradient(135deg,rgba(127,90,240,.3),rgba(127,90,240,.05));color:var(--purple);box-shadow:0 0 20px rgba(127,90,240,.2)}
.feat-card h3{font-size:1.15rem;font-weight:700;margin-bottom:10px}
.feat-card p{color:rgba(255,255,255,.55);font-size:.9rem;line-height:1.6}
.feat-glow{position:absolute;bottom:-40px;right:-40px;width:120px;height:120px;border-radius:50%;opacity:.12;transition:.4s}
.feat-card:hover .feat-glow{opacity:.3}

/* ── STATS ── */
.stats{background:linear-gradient(135deg,rgba(108,99,255,.08),rgba(0,229,255,.05));border-top:1px solid var(--glass-border);border-bottom:1px solid var(--glass-border)}
.stats-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:40px;text-align:center}
.stat-item{padding:20px 0}
.stat-num{font-size:clamp(2.5rem,5vw,3.8rem);font-weight:900;background:linear-gradient(135deg,var(--violet),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;line-height:1;margin-bottom:8px}
.stat-label{color:rgba(255,255,255,.55);font-size:.9rem;font-weight:500}

/* ── GALLERY ── */
.gallery-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:60px}
.gallery-card{border-radius:20px;overflow:hidden;aspect-ratio:16/9;position:relative;cursor:none;border:1px solid var(--glass-border)}
.gallery-card .inner{width:100%;height:100%;display:flex;align-items:center;justify-content:center;font-size:2rem;font-weight:800;letter-spacing:-.02em;transition:transform .5s cubic-bezier(.34,1.56,.64,1)}
.gallery-card:hover .inner{transform:scale(1.08)}
.gc1{background:linear-gradient(135deg,#6C63FF,#00E5FF)}
.gc2{background:linear-gradient(135deg,#FF4ECD,#FFD93D)}
.gc3{background:linear-gradient(135deg,#00FFA3,#00E5FF)}
.gc4{background:linear-gradient(135deg,#7F5AF0,#FF4ECD)}
.gc5{background:linear-gradient(135deg,#FFD93D,#00FFA3)}
.gc6{background:linear-gradient(135deg,#00E5FF,#7F5AF0)}
.gallery-card .overlay{position:absolute;inset:0;background:rgba(0,0,0,.5);display:flex;align-items:center;justify-content:center;opacity:0;transition:.3s;backdrop-filter:blur(4px)}
.gallery-card:hover .overlay{opacity:1}
.overlay-text{color:#fff;font-weight:700;font-size:1rem;transform:translateY(10px);transition:.3s .05s}
.gallery-card:hover .overlay-text{transform:translateY(0)}

/* ── TESTIMONIALS ── */
.testi-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:24px;margin-top:60px}
.testi-card{background:var(--glass);border:1px solid var(--glass-border);border-radius:20px;padding:32px;backdrop-filter:blur(20px);transition:.4s;position:relative}
.testi-card:hover{transform:translateY(-6px);border-color:rgba(108,99,255,.4);box-shadow:0 20px 50px rgba(0,0,0,.3)}
.stars{color:var(--yellow);font-size:.9rem;margin-bottom:16px;letter-spacing:2px}
.testi-card p{color:rgba(255,255,255,.7);font-size:.95rem;line-height:1.7;margin-bottom:24px}
.testi-author{display:flex;align-items:center;gap:12px}
.author-avatar{width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:700;font-size:.9rem;flex-shrink:0}
.av1{background:linear-gradient(135deg,var(--violet),var(--cyan))}
.av2{background:linear-gradient(135deg,var(--pink),var(--yellow))}
.av3{background:linear-gradient(135deg,var(--green),var(--cyan))}
.author-name{font-weight:700;font-size:.95rem}
.author-role{font-size:.8rem;color:rgba(255,255,255,.45)}
.testi-quote{position:absolute;top:20px;right:24px;font-size:3rem;color:rgba(108,99,255,.15);line-height:1;font-family:serif}

/* ── PRICING ── */
.pricing-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:24px;margin-top:60px}
.price-card{background:var(--glass);border:1px solid var(--glass-border);border-radius:24px;padding:40px 32px;backdrop-filter:blur(20px);transition:.4s;position:relative;overflow:hidden}
.price-card.featured{border-color:var(--violet);background:linear-gradient(135deg,rgba(108,99,255,.12),rgba(0,229,255,.06))}
.price-card.featured::before{content:'';position:absolute;inset:0;background:linear-gradient(135deg,rgba(108,99,255,.05),transparent);pointer-events:none}
.price-badge{position:absolute;top:20px;right:20px;padding:4px 12px;border-radius:50px;background:linear-gradient(135deg,var(--violet),var(--cyan));color:#fff;font-size:.72rem;font-weight:700}
.price-card:hover{transform:translateY(-8px);box-shadow:0 30px 60px rgba(0,0,0,.3)}
.price-name{font-size:.85rem;font-weight:700;text-transform:uppercase;letter-spacing:.1em;color:var(--violet);margin-bottom:12px}
.price-amount{font-size:3.2rem;font-weight:900;line-height:1;margin-bottom:6px}
.price-amount sup{font-size:1.4rem;vertical-align:super;font-weight:600}
.price-period{font-size:.85rem;color:rgba(255,255,255,.45);margin-bottom:28px}
.price-divider{height:1px;background:var(--glass-border);margin:24px 0}
.price-features{list-style:none;display:flex;flex-direction:column;gap:12px;margin-bottom:32px}
.price-features li{display:flex;align-items:center;gap:10px;font-size:.9rem;color:rgba(255,255,255,.75)}
.price-features li i{color:var(--green);font-size:.85rem}
.price-features li.off{color:rgba(255,255,255,.3)}
.price-features li.off i{color:rgba(255,255,255,.2)}
.price-btn{width:100%;padding:13px;border-radius:12px;font-family:'Poppins',sans-serif;font-weight:700;font-size:.95rem;border:none;cursor:none;transition:.3s}
.price-btn.primary{background:linear-gradient(135deg,var(--violet),var(--purple));color:#fff;box-shadow:0 0 25px rgba(108,99,255,.4)}
.price-btn.primary:hover{box-shadow:0 0 40px rgba(108,99,255,.6);transform:translateY(-2px)}
.price-btn.secondary{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.2)}
.price-btn.secondary:hover{border-color:var(--violet);background:rgba(108,99,255,.1)}

/* ── FOOTER ── */
footer{position:relative;z-index:2;background:linear-gradient(180deg,transparent,var(--dark3));overflow:hidden;padding-top:0}
.wave-wrap{line-height:0;margin-bottom:-2px}
.wave-wrap svg{display:block;width:100%}
.footer-inner{padding:60px 5% 40px}
.footer-top{display:grid;grid-template-columns:2fr repeat(3,1fr);gap:40px;margin-bottom:50px}
.footer-brand .nav-logo{display:inline-block;margin-bottom:16px;font-size:1.5rem}
.footer-brand p{color:rgba(255,255,255,.5);font-size:.9rem;line-height:1.7;max-width:300px}
.footer-social{display:flex;gap:12px;margin-top:20px}
.social-link{width:38px;height:38px;border-radius:10px;background:var(--glass);border:1px solid var(--glass-border);display:flex;align-items:center;justify-content:center;color:rgba(255,255,255,.6);text-decoration:none;transition:.3s;font-size:.9rem}
.social-link:hover{background:var(--violet);color:#fff;border-color:var(--violet);box-shadow:0 0 20px rgba(108,99,255,.4);transform:translateY(-3px)}
.footer-col h4{font-size:.9rem;font-weight:700;margin-bottom:18px;color:#fff}
.footer-col ul{list-style:none;display:flex;flex-direction:column;gap:10px}
.footer-col ul a{color:rgba(255,255,255,.5);text-decoration:none;font-size:.875rem;transition:.3s;display:inline-block}
.footer-col ul a:hover{color:#fff;transform:translateX(4px)}
.footer-bottom{border-top:1px solid var(--glass-border);padding-top:28px;display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:16px}
.footer-bottom p{color:rgba(255,255,255,.35);font-size:.82rem}
.footer-bottom span{background:linear-gradient(135deg,var(--violet),var(--cyan));-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:600}

/* ── WAVE ── */
.wave-path{animation:waveAnim 6s ease-in-out infinite alternate}
@keyframes waveAnim{0%{d:path("M0,96 C240,150 480,30 720,96 C960,162 1200,42 1440,96 L1440,200 L0,200 Z")}100%{d:path("M0,96 C240,42 480,162 720,96 C960,30 1200,150 1440,96 L1440,200 L0,200 Z")}}

/* ── GENERIC ANIMS ── */
@keyframes fadeSlideUp{from{opacity:0;transform:translateY(30px)}to{opacity:1;transform:translateY(0)}}
@keyframes floatY{0%,100%{transform:translateY(0)}50%{transform:translateY(-10px)}}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.6}}
@keyframes rotate{to{transform:rotate(360deg)}}

/* ── RIPPLE ── */
.ripple-btn{position:relative;overflow:hidden}
.ripple-btn .ripple{position:absolute;border-radius:50%;background:rgba(255,255,255,.3);transform:scale(0);animation:rippleAnim .6s linear;pointer-events:none}
@keyframes rippleAnim{to{transform:scale(4);opacity:0}}

/* ── RESPONSIVE ── */
@media(max-width:768px){
  .nav-links,.nav-cta{display:none}
  .hamburger{display:flex}
  .footer-top{grid-template-columns:1fr 1fr}
  .footer-brand{grid-column:1/-1}
}
@media(max-width:480px){
  .footer-top{grid-template-columns:1fr}
  .hero-btns{flex-direction:column;align-items:center}
}
</style>
</head>
<body>

<!-- Loading Screen -->
<div id="loading">
  <div class="load-logo">✦ AnimLib</div>
  <div class="load-bar-wrap"><div class="load-bar"></div></div>
  <p style="color:rgba(255,255,255,.4);font-size:.8rem">Initializing animations…</p>
</div>

<!-- Scroll Progress -->
<div id="scroll-progress"></div>

<!-- Custom Cursor -->
<div id="cursor"></div>
<div id="cursor-follower"></div>

<!-- Background Elements -->
<div id="particles-js"></div>
<div class="blob blob1"></div>
<div class="blob blob2"></div>
<div class="blob blob3"></div>

<!-- Dark Mode Toggle -->
<button id="dm-toggle" title="Toggle theme"><i class="fas fa-moon"></i></button>

<!-- Back to Top -->
<button id="back-top" onclick="window.scrollTo({top:0,behavior:'smooth'})"><i class="fas fa-arrow-up"></i></button>

<!-- Chatbot Button -->
<button id="chatbot-btn" title="Chat with us"><i class="fas fa-comment-dots"></i></button>

<!-- ── NAVIGATION ── -->
<nav class="nav">
  <a href="#" class="nav-logo">✦ AnimLib</a>
  <ul class="nav-links">
    <li><a href="#">Home</a></li>
    <li><a href="#features">Animations</a></li>
    <li><a href="#gallery">Components</a></li>
    <li><a href="#pricing">Pricing</a></li>
    <li><a href="#footer">Contact</a></li>
  </ul>
  <a href="#pricing" class="nav-cta">Get Started</a>
  <div class="hamburger" id="hamburger"><span></span><span></span><span></span></div>
</nav>

<!-- Mobile Menu -->
<div class="mobile-menu" id="mobile-menu">
  <a href="#">Home</a>
  <a href="#features">Animations</a>
  <a href="#gallery">Components</a>
  <a href="#pricing">Pricing</a>
  <a href="#footer">Contact</a>
</div>

<!-- ── HERO ── -->
<section class="hero">
  <div class="hero-glow"></div>
  <div>
    <div class="hero-badge"><span class="dot"></span>New — 500+ animations just added</div>
    <h1>
      <span class="typing-wrap" id="typing-text"></span><span class="typing-cursor"></span>
      <span class="grad">Animation Library</span>
    </h1>
    <p class="hero-subtitle">Explore thousands of beautiful CSS, JavaScript, SVG and Motion animations — production-ready and free to use.</p>
    <div class="hero-btns">
      <a href="#gallery" class="btn-primary ripple-btn"><span>Explore Library</span></a>
      <a href="#pricing" class="btn-outline">Get Started →</a>
    </div>
  </div>
  <div class="hero-scroll">
    <span>Scroll</span>
    <div class="scroll-line"></div>
  </div>
</section>

<!-- ── FEATURES ── -->
<section id="features">
  <div class="text-center" data-aos="fade-up">
    <div class="section-label">What We Offer</div>
    <h2 class="section-title">Every animation type,<br>in one place.</h2>
    <p class="section-sub">From micro-interactions to full-page sequences — browse, copy, ship.</p>
  </div>
  <div class="features-grid">
    <div class="feat-card" data-aos="fade-up" data-aos-delay="0">
      <div class="feat-icon c1"><i class="fas fa-palette"></i></div>
      <div class="feat-glow" style="background:var(--violet)"></div>
      <h3>CSS Animations</h3>
      <p>Pure CSS keyframes, transitions, and transforms. Zero JS overhead, silky-smooth performance.</p>
    </div>
    <div class="feat-card" data-aos="fade-up" data-aos-delay="80">
      <div class="feat-icon c2"><i class="fab fa-js-square"></i></div>
      <div class="feat-glow" style="background:var(--cyan)"></div>
      <h3>JavaScript Effects</h3>
      <p>Vanilla JS and Web Animations API — parallax, scroll-driven, and pointer-tracking effects.</p>
    </div>
    <div class="feat-card" data-aos="fade-up" data-aos-delay="160">
      <div class="feat-icon c3"><i class="fas fa-bolt"></i></div>
      <div class="feat-glow" style="background:var(--green)"></div>
      <h3>GSAP Motion</h3>
      <p>Timeline-based sequencing with eases, stagger, and ScrollTrigger integrations included.</p>
    </div>
    <div class="feat-card" data-aos="fade-up" data-aos-delay="240">
      <div class="feat-icon c4"><i class="fas fa-draw-polygon"></i></div>
      <div class="feat-glow" style="background:var(--pink)"></div>
      <h3>SVG Animation</h3>
      <p>Path morphing, stroke draws, and complex SVG choreography powered by modern web standards.</p>
    </div>
    <div class="feat-card" data-aos="fade-up" data-aos-delay="320">
      <div class="feat-icon c5"><i class="fas fa-cube"></i></div>
      <div class="feat-glow" style="background:var(--yellow)"></div>
      <h3>3D Effects</h3>
      <p>CSS 3D transforms and Three.js scenes — cards, spheres, and layered depth effects.</p>
    </div>
    <div class="feat-card" data-aos="fade-up" data-aos-delay="400">
      <div class="feat-icon c6"><i class="fas fa-spinner"></i></div>
      <div class="feat-glow" style="background:var(--purple)"></div>
      <h3>Loading Animations</h3>
      <p>Spinners, skeleton screens, progress bars, and reveal loaders in every style imaginable.</p>
    </div>
  </div>
</section>

<!-- ── STATS ── -->
<section class="stats">
  <div class="stats-grid">
    <div class="stat-item" data-aos="zoom-in" data-aos-delay="0">
      <div class="stat-num" data-count="10000">0</div>
      <div class="stat-label">Animations</div>
    </div>
    <div class="stat-item" data-aos="zoom-in" data-aos-delay="100">
      <div class="stat-num" data-count="500">0</div>
      <div class="stat-label">Components</div>
    </div>
    <div class="stat-item" data-aos="zoom-in" data-aos-delay="200">
      <div class="stat-num" data-count="250000">0</div>
      <div class="stat-label">Users</div>
    </div>
    <div class="stat-item" data-aos="zoom-in" data-aos-delay="300">
      <div class="stat-num" data-count="99">0</div>
      <div class="stat-label">Performance Score</div>
    </div>
  </div>
</section>

<!-- ── GALLERY ── -->
<section id="gallery">
  <div class="text-center" data-aos="fade-up">
    <div class="section-label">Preview</div>
    <h2 class="section-title">Live animation gallery</h2>
    <p class="section-sub">Hover over any card to see the effect in action.</p>
  </div>
  <div class="gallery-grid">
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="0">
      <div class="inner gc1">Fade & Slide</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="60">
      <div class="inner gc2">Neon Glow</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="120">
      <div class="inner gc3">Morph Path</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="180">
      <div class="inner gc4">Parallax</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="240">
      <div class="inner gc5">3D Flip</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
    <div class="gallery-card" data-aos="zoom-in" data-aos-delay="300">
      <div class="inner gc6">Liquid</div>
      <div class="overlay"><div class="overlay-text">View Animation →</div></div>
    </div>
  </div>
</section>

<!-- ── TESTIMONIALS ── -->
<section>
  <div class="text-center" data-aos="fade-up">
    <div class="section-label">Testimonials</div>
    <h2 class="section-title">Loved by builders worldwide</h2>
    <p class="section-sub">Thousands of developers and designers ship faster with AnimLib.</p>
  </div>
  <div class="testi-grid">
    <div class="testi-card" data-aos="fade-up" data-aos-delay="0">
      <div class="testi-quote">"</div>
      <div class="stars">★★★★★</div>
      <p>AnimLib cut our frontend animation time in half. The GSAP presets alone are worth it — I used to spend hours on sequencing, now it's minutes.</p>
      <div class="testi-author">
        <div class="author-avatar av1">AK</div>
        <div><div class="author-name">Alex Kim</div><div class="author-role">Lead Engineer @ Vercel</div></div>
      </div>
    </div>
    <div class="testi-card" data-aos="fade-up" data-aos-delay="120">
      <div class="testi-quote">"</div>
      <div class="stars">★★★★★</div>
      <p>The SVG animation collection is unlike anything else I've found. Every path morphing example just works and looks breathtaking on mobile too.</p>
      <div class="testi-author">
        <div class="author-avatar av2">SL</div>
        <div><div class="author-name">Sara Lin</div><div class="author-role">Product Designer @ Framer</div></div>
      </div>
    </div>
    <div class="testi-card" data-aos="fade-up" data-aos-delay="240">
      <div class="testi-quote">"</div>
      <div class="stars">★★★★★</div>
      <p>I rebuilt our whole design system's motion layer using AnimLib. Client reactions went from "it's fine" to "how did you build that?" every time.</p>
      <div class="testi-author">
        <div class="author-avatar av3">MR</div>
        <div><div class="author-name">Marco Rossi</div><div class="author-role">Creative Director @ Linear</div></div>
      </div>
    </div>
  </div>
</section>

<!-- ── PRICING ── -->
<section id="pricing">
  <div class="text-center" data-aos="fade-up">
    <div class="section-label">Pricing</div>
    <h2 class="section-title">Simple, transparent pricing</h2>
    <p class="section-sub">Start free, scale as you grow. No hidden fees.</p>
  </div>
  <div class="pricing-grid">
    <div class="price-card" data-aos="fade-up" data-aos-delay="0">
      <div class="price-name">Starter</div>
      <div class="price-amount"><sup>$</sup>0</div>
      <div class="price-period">Free forever</div>
      <div class="price-divider"></div>
      <ul class="price-features">
        <li><i class="fas fa-check-circle"></i> 200 animations</li>
        <li><i class="fas fa-check-circle"></i> CSS & JS only</li>
        <li><i class="fas fa-check-circle"></i> Community support</li>
        <li class="off"><i class="fas fa-times-circle"></i> GSAP presets</li>
        <li class="off"><i class="fas fa-times-circle"></i> Commercial license</li>
      </ul>
      <button class="price-btn secondary">Get Started Free</button>
    </div>
    <div class="price-card featured" data-aos="fade-up" data-aos-delay="100">
      <div class="price-badge">Most Popular</div>
      <div class="price-name">Pro</div>
      <div class="price-amount"><sup>$</sup>19</div>
      <div class="price-period">per month, billed annually</div>
      <div class="price-divider"></div>
      <ul class="price-features">
        <li><i class="fas fa-check-circle"></i> All 10,000+ animations</li>
        <li><i class="fas fa-check-circle"></i> GSAP & SVG presets</li>
        <li><i class="fas fa-check-circle"></i> Commercial license</li>
        <li><i class="fas fa-check-circle"></i> Priority support</li>
        <li><i class="fas fa-check-circle"></i> New drops monthly</li>
      </ul>
      <button class="price-btn primary">Start Pro Trial</button>
    </div>
    <div class="price-card" data-aos="fade-up" data-aos-delay="200">
      <div class="price-name">Enterprise</div>
      <div class="price-amount"><sup>$</sup>99</div>
      <div class="price-period">per month, billed annually</div>
      <div class="price-divider"></div>
      <ul class="price-features">
        <li><i class="fas fa-check-circle"></i> Everything in Pro</li>
        <li><i class="fas fa-check-circle"></i> Unlimited team seats</li>
        <li><i class="fas fa-check-circle"></i> Custom animations</li>
        <li><i class="fas fa-check-circle"></i> Dedicated account manager</li>
        <li><i class="fas fa-check-circle"></i> SLA guarantee</li>
      </ul>
      <button class="price-btn secondary">Contact Sales</button>
    </div>
  </div>
</section>

<!-- ── FOOTER ── -->
<footer id="footer">
  <div class="wave-wrap">
    <svg viewBox="0 0 1440 120" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">
      <path class="wave-path" d="M0,60 C240,100 480,20 720,60 C960,100 1200,20 1440,60 L1440,120 L0,120 Z" fill="#1a1a2e" />
    </svg>
  </div>
  <div class="footer-inner">
    <div class="footer-top">
      <div class="footer-brand">
        <a href="#" class="nav-logo">✦ AnimLib</a>
        <p>The internet's largest curated collection of web animations — built for designers and engineers who move fast.</p>
        <div class="footer-social">
          <a href="#" class="social-link"><i class="fab fa-twitter"></i></a>
          <a href="#" class="social-link"><i class="fab fa-github"></i></a>
          <a href="#" class="social-link"><i class="fab fa-discord"></i></a>
          <a href="#" class="social-link"><i class="fab fa-youtube"></i></a>
        </div>
      </div>
      <div class="footer-col">
        <h4>Product</h4>
        <ul>
          <li><a href="#">Animations</a></li>
          <li><a href="#">Components</a></li>
          <li><a href="#">Templates</a></li>
          <li><a href="#">Changelog</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Company</h4>
        <ul>
          <li><a href="#">About</a></li>
          <li><a href="#">Blog</a></li>
          <li><a href="#">Careers</a></li>
          <li><a href="#">Contact</a></li>
        </ul>
      </div>
      <div class="footer-col">
        <h4>Legal</h4>
        <ul>
          <li><a href="#">Privacy</a></li>
          <li><a href="#">Terms</a></li>
          <li><a href="#">License</a></li>
          <li><a href="#">Cookies</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <p>© 2026 <span>AnimLib</span>. All rights reserved.</p>
      <p>Made with <span>♥</span> for the web</p>
    </div>
  </div>
</footer>

<script>
// ── LOADING SCREEN ──
window.addEventListener('load', () => {
  setTimeout(() => document.getElementById('loading').classList.add('hidden'), 1900);
});

// ── CUSTOM CURSOR ──
const cursor = document.getElementById('cursor');
const follower = document.getElementById('cursor-follower');
let fx = 0, fy = 0, cx = 0, cy = 0;
document.addEventListener('mousemove', e => {
  cx = e.clientX; cy = e.clientY;
  cursor.style.left = cx + 'px'; cursor.style.top = cy + 'px';
});
(function animFollower() {
  fx += (cx - fx) * 0.12; fy += (cy - fy) * 0.12;
  follower.style.left = fx + 'px'; follower.style.top = fy + 'px';
  requestAnimationFrame(animFollower);
})();
document.querySelectorAll('a,button,[data-hover]').forEach(el => {
  el.addEventListener('mouseenter', () => { cursor.style.transform='translate(-50%,-50%) scale(2.5)'; cursor.style.background='var(--pink)'; follower.style.transform='translate(-50%,-50%) scale(1.5)'; follower.style.borderColor='rgba(255,78,205,.4)' });
  el.addEventListener('mouseleave', () => { cursor.style.transform='translate(-50%,-50%) scale(1)'; cursor.style.background='var(--cyan)'; follower.style.transform='translate(-50%,-50%) scale(1)'; follower.style.borderColor='rgba(108,99,255,.5)' });
});

// ── SCROLL PROGRESS ──
const bar = document.getElementById('scroll-progress');
window.addEventListener('scroll', () => {
  const pct = window.scrollY / (document.documentElement.scrollHeight - window.innerHeight) * 100;
  bar.style.width = pct + '%';
  document.getElementById('back-top').classList.toggle('visible', window.scrollY > 400);
});

// ── HAMBURGER ──
document.getElementById('hamburger').addEventListener('click', function() {
  this.classList.toggle('open');
  document.getElementById('mobile-menu').classList.toggle('open');
});
document.getElementById('mobile-menu').querySelectorAll('a').forEach(a => {
  a.addEventListener('click', () => {
    document.getElementById('hamburger').classList.remove('open');
    document.getElementById('mobile-menu').classList.remove('open');
  });
});

// ── DARK MODE ──
document.getElementById('dm-toggle').addEventListener('click', function() {
  document.body.classList.toggle('light-mode');
  this.querySelector('i').className = document.body.classList.contains('light-mode') ? 'fas fa-sun' : 'fas fa-moon';
});

// ── RIPPLE ──
document.querySelectorAll('.ripple-btn').forEach(btn => {
  btn.addEventListener('click', function(e) {
    const r = document.createElement('span'); r.className = 'ripple';
    const size = Math.max(this.offsetWidth, this.offsetHeight);
    const rect = this.getBoundingClientRect();
    r.style.cssText = `width:${size}px;height:${size}px;left:${e.clientX-rect.left-size/2}px;top:${e.clientY-rect.top-size/2}px`;
    this.appendChild(r); setTimeout(() => r.remove(), 600);
  });
});

// ── AOS ──
AOS.init({ duration: 700, easing: 'ease-out-cubic', once: true, offset: 60 });

// ── PARTICLES.JS ──
particlesJS('particles-js', {
  particles: {
    number: { value: 60, density: { enable: true, value_area: 900 } },
    color: { value: ['#6C63FF','#00E5FF','#FF4ECD','#00FFA3'] },
    shape: { type: 'circle' },
    opacity: { value: 0.35, random: true, anim: { enable: true, speed: 0.8, opacity_min: 0.05, sync: false } },
    size: { value: 2.5, random: true },
    line_linked: { enable: true, distance: 130, color: '#6C63FF', opacity: 0.12, width: 1 },
    move: { enable: true, speed: 0.8, direction: 'none', random: true, straight: false, out_mode: 'out', bounce: false }
  },
  interactivity: {
    detect_on: 'window',
    events: { onhover: { enable: true, mode: 'grab' }, onclick: { enable: true, mode: 'push' }, resize: true },
    modes: { grab: { distance: 160, line_linked: { opacity: 0.4 } }, push: { particles_nb: 3 } }
  },
  retina_detect: true
});

// ── TYPING EFFECT ──
const words = ['Unlimited ','Beautiful ','Production-Ready ','Smooth '];
let wi = 0, ci = 0, deleting = false;
const el = document.getElementById('typing-text');
function typeLoop() {
  const word = words[wi];
  el.textContent = deleting ? word.slice(0, ci--) : word.slice(0, ci++);
  if (!deleting && ci > word.length) { deleting = true; setTimeout(typeLoop, 1200); return; }
  if (deleting && ci < 0) { deleting = false; ci = 0; wi = (wi + 1) % words.length; setTimeout(typeLoop, 300); return; }
  setTimeout(typeLoop, deleting ? 50 : 90);
}
setTimeout(typeLoop, 1200);

// ── COUNTER ANIMATION ──
function animateCounter(el, target) {
  const suffixes = { 10000: '+', 500: '+', 250000: 'K+', 99: '%' };
  const suffix = suffixes[target] || '';
  const display = target >= 1000 ? Math.round(target / 1000) : target;
  let start = 0; const duration = 2000; const step = 16;
  const increment = display / (duration / step);
  const timer = setInterval(() => {
    start += increment;
    if (start >= display) { el.textContent = display + suffix; clearInterval(timer); }
    else el.textContent = Math.floor(start) + suffix;
  }, step);
}
const statObserver = new IntersectionObserver(entries => {
  entries.forEach(e => {
    if (e.isIntersecting) { animateCounter(e.target, +e.target.dataset.count); statObserver.unobserve(e.target); }
  });
}, { threshold: 0.5 });
document.querySelectorAll('[data-count]').forEach(el => statObserver.observe(el));

// ── GSAP HERO ──
if (window.gsap) {
  gsap.registerPlugin(ScrollTrigger);
  gsap.from('.hero h1', { opacity: 0, y: 60, duration: 1, ease: 'power3.out', delay: 2 });
  gsap.from('.hero-subtitle', { opacity: 0, y: 40, duration: 1, ease: 'power3.out', delay: 2.2 });
  gsap.from('.hero-btns', { opacity: 0, y: 30, duration: 1, ease: 'power3.out', delay: 2.4 });
  document.querySelectorAll('.feat-card').forEach((card, i) => {
    gsap.to(card, { y: -6, duration: 2 + i * 0.15, ease: 'sine.inOut', yoyo: true, repeat: -1, delay: i * 0.2 });
  });
}
</script>
</body>
</html>"""

@app.route("/")
def index():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(debug=True)
