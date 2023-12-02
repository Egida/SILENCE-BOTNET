<!DOCTYPE html>
<html lang="en"><head><meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
	
        <title>SILENCE API</title>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta property="og:type" content="website">
        <meta property="og:title" content="&#39;">
        <meta property="og:url" content="https:///">
        <meta name="twitter:card" content="summary_large_image">
        <meta property="twitter:image" content="https://i.imgur.com/a/4OmxUkU.gif">
        <meta name="theme-color" content="#2f3136">
        <link rel="stylesheet" href="./assets/css/main.css">
    </head>
    <body>
        <main>
            <script>
                function audioPlay() {
                    var audio = document.getElementById("audio");
                    audio.volume = 0.4;
                    audio.play()
                }
                function videoPlay() {
                    var video = document.getElementById("video");
                    video.play()
                }
            </script>
            <input type="checkbox" autocomplete="off" id="overlay-toggle">
            <div class="overlay fullscreen">
                <label for="overlay-toggle" onclick="audioPlay();videoPlay()">
                    <span class="no-hover" style="font-family: derk; font-size: 0.6em;">press anywhere</span>
                    <span class="hover" style="font-family: derk; font-size: 0.6em;">click anywhere</span>
                </label>
            </div>
            <audio loop="" preload="auto" id="audio">
                <source src="assets/audio/audio.mp3" type="audio/mp3">
            </audio>
            <video muted="muted" loop="" playsinline="" preload="auto" class="fullscreen bg-video" id="video">
                <source src="assets/images/bg.mp4" type="video/mp4">
            </video>
            <section class="fullscreen text-content">
            
            <div id="manipulate">
                <h1></h1>
            </div>
            <div id="manipulate1">
            </div>
            <div id="center">
                <h1 style="font-family: derk; text-shadow: 0 0 0.40em #bababa;">SILENCE API</h1>
                <div class="socials">
		<h4></h4>

                    <span>
                        ▶:
                <a href="https://t.me/silencenetworks" style="text-decoration:none; font-family: derk; font-size: 1em;">Telegram</a>
                    </span>


                    <span>
                        ▶:
                <a href="rules.php" style="text-decoration:none; font-family: derk; font-size: 1em;">API Rules</a>
                    </span>
                    
                    <span>
                        ▶:
                <a href="methods.php" style="text-decoration:none; font-family: derk; font-size: 1em;">API Methods</a>
                    </span>

                    <span>
                        ▶:
                <a href="pricing.php" style="text-decoration:none; font-family: derk; font-size: 1em;">Pricing</a>
                    </span>
                    
            </div>
        </div></section></main>

</body></html>