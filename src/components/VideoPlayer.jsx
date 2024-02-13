import React, { useEffect, useState } from "react";

const VideoPlayer = () => {
  const [videoFrames, setVideoFrames] = useState("");

  useEffect(() => {
   const fetchVideoFrames = async () => {
     try {
       const response = await fetch("http://127.0.0.1:5000/video_feed");
       console.log("response: ", response);
       if (!response.ok) {
         throw new Error(`HTTP error! Status: ${response.status}`);
       }
       console.log("status: ", response.status);
       const blob = await response.blob(); // Correct way to extract Blob from response
       if (!blob) {
         throw new Error("Blob empty");
       }
       else {
         console.log(blob);
       }
       const url = URL.createObjectURL(blob);
       if (!url)
         throw new error("eroorr");
       
       console.log("url is:",url)
       setVideoFrames(url);
     } catch (error) {
       console.error("Error fetching video frames:", error);
     }
   };

    fetchVideoFrames();
  }, []); // Empty dependency array ensures the effect runs only once when the component mounts

  // Add logic for overlay, box, or other visual elements

  return (
    <div>
      <video controls autoPlay>
        <source
          src="http://127.0.0.1:5000/video_feed"
          type="multipart/x-mixed-replace; boundary=frame"
        />
        Your browser does not support the video tag.
      </video>
      {/* Add overlay elements here */}
    </div>
  );
};

export default VideoPlayer;
