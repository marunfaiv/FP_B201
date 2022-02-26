import React from "react"
import "./styles.css"

export default function LandingPageDesktop() {
  return (
    <div className="landing-page-desktop flex-col-hstart-vstart clip-contents">
      <div className="flex-col-hend">
        <div className="title-_box flex-col-hstart-vstart">
          <p className="txt-430 flex-hcenter">REAL-TIME WATCHER</p>
        </div>
        <div className="group-446 flex-col">
          <div className="cam-_frame" />
          <div className="folder-_button flex-col-hstart-vstart">
            <p className="txt-1056 flex-hcenter">HISTORY</p>
          </div>
        </div>
      </div>
    </div>
  )
}