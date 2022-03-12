import cv from "opencv.js";

function cameraCapture() {
  let video = document.getElementById("videoInput");
  video.width = 1706;
  video.height = 752;
  navigator.mediaDevices
    .getUserMedia({ video: true, audio: false })
    .then(function (stream) {
      video.srcObject = stream;
      video.play();
      let src = new cv.Mat(video.height, video.width, cv.CV_8UC4);
      let cap = new cv.VideoCapture(video);

      const FPS = 30;
      function processVideo() {
        try {
          let begin = Date.now();
          cap.read(src);
          let delay = 1000 / FPS - (Date.now() - begin);
          setTimeout(processVideo, delay);
        } catch (err) {
          console.error(err);
        }
      }
      //   schedule the first one.
      setTimeout(processVideo, 0);
    })
    .catch(function (err) {
      console.log("An error occured! " + err);
    });
}
