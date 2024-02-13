import React from "react";
import VideoPlayer from "./components/VideoPlayer"; // Import the VideoPlayer component

const App = () => {
  // const rtspUrl = "static/video.mp4";

  return(
    <div>
      <h1>RTSP Video Player</h1>
      <VideoPlayer />
    </div>
  );
};

export default App;
