<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Stopwatch</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background: #222;
      color: #fff;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      flex-direction: column;
    }

    .stopwatch {
      text-align: center;
    }

    #display {
      font-size: 4em;
      margin-bottom: 20px;
    }

    .buttons button {
      padding: 10px 20px;
      margin: 5px;
      font-size: 1em;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      transition: background 0.3s;
    }

    .buttons button:hover {
      background: #444;
    }

    .lap-list {
      margin-top: 20px;
      max-height: 200px;
      overflow-y: auto;
      width: 100%;
      max-width: 300px;
      text-align: left;
    }

    .lap-item {
      background: #333;
      padding: 10px;
      margin: 5px 0;
      border-radius: 5px;
    }
  </style>
</head>
<body>

  <div class="stopwatch">
    <div id="display">00:00:00</div>
    <div class="buttons">
      <button onclick="startStopwatch()">Start</button>
      <button onclick="pauseStopwatch()">Pause</button>
      <button onclick="resetStopwatch()">Reset</button>
      <button onclick="recordLap()">Lap</button>
    </div>
    <div class="lap-list" id="laps"></div>
  </div>

  <script>
    let startTime, elapsedTime = 0, timerInterval;

    function updateDisplay(time) {
      const date = new Date(time);
      const minutes = String(date.getUTCMinutes()).padStart(2, '0');
      const seconds = String(date.getUTCSeconds()).padStart(2, '0');
      const milliseconds = String(Math.floor(date.getUTCMilliseconds() / 10)).padStart(2, '0');
      document.getElementById('display').textContent = ${minutes}:${seconds}:${milliseconds};
    }

    function startStopwatch() {
      if (!timerInterval) {
        startTime = Date.now() - elapsedTime;
        timerInterval = setInterval(() => {
          elapsedTime = Date.now() - startTime;
          updateDisplay(elapsedTime);
        }, 10);
      }
    }

    function pauseStopwatch() {
      clearInterval(timerInterval);
      timerInterval = null;
    }

    function resetStopwatch() {
      clearInterval(timerInterval);
      timerInterval = null;
      elapsedTime = 0;
      updateDisplay(0);
      document.getElementById('laps').innerHTML = '';
    }

    function recordLap() {
      if (elapsedTime > 0) {
        const lapTime = document.createElement('div');
        lapTime.className = 'lap-item';
        lapTime.textContent = document.getElementById('display').textContent;
        document.getElementById('laps').appendChild(lapTime);
      }
    }
  </script>

</body>
</html>
