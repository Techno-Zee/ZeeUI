/** @odoo-module **/
import { Chatter } from "@mail/chatter/web_portal/chatter";
import { patch } from "@web/core/utils/patch";
import { useRef } from "@odoo/owl";

// Patch the Chatter class to add camera functionality
patch(Chatter.prototype, {
    setup() {
        super.setup();
        this.video = useRef("video");
        this.stop_camera = useRef("stop-camera-button");
        this.canvas = useRef("canvas");
    },
    onClickCamera: function() {
        var self = this;
        var myModal = document.getElementById("myModal");
        myModal.style.display = "block";

        // Deteksi jika perangkat adalah Android
        let isAndroid = /Android/i.test(navigator.userAgent);
        
        if (isAndroid) {
            // Gunakan aplikasi kamera bawaan Android
            let input = document.createElement("input");
            input.type = "file";
            input.accept = "image/*";
            input.capture = "environment";
            
            input.addEventListener("change", function(event) {
                let file = event.target.files[0];
                if (file) {
                    self.attachmentUploader.uploadFile(file);
                }
                myModal.style.display = "none";
            });
            
            input.click();
        } else {
            // Metode standar untuk perangkat non-Android
            let constraints = {
                audio: false,
                video: { facingMode: { ideal: "environment" } }
            };

            navigator.mediaDevices
                .getUserMedia(constraints)
                .then(function(vidStream) {
                    var video = self.video.el;
                    if ("srcObject" in video) {
                        video.srcObject = vidStream;
                    } else {
                        video.src = window.URL.createObjectURL(vidStream);
                    }
                    video.onloadedmetadata = function() {
                        video.play();
                    };

                    var stopButton = self.stop_camera.el;
                    stopButton.addEventListener("click", function() {
                        vidStream.getTracks().forEach(function(track) {
                            track.stop();
                        });
                        myModal.style.display = "none";
                    });
                })
                .catch(function(e) {
                    console.error("Error accessing media devices:", e.message);
                    alert("Tidak dapat mengakses kamera: " + e.message);
                });
        }
    },
    ImageCapture: function() {
        let canvas = this.canvas.el;
        let video = this.video.el;
        
        canvas.width = video.videoWidth;
        canvas.height = video.videoHeight;
        canvas.getContext("2d").drawImage(video, 0, 0, canvas.width, canvas.height);
        
        let image_data_url = canvas.toDataURL("image/jpeg", 1.0);
        let [header, base64Data] = image_data_url.split(",");
        let mime = header.match(/:(.*?);/)[1];
        let binary = atob(base64Data);
        let u8arr = new Uint8Array(binary.length);
        
        for (let i = 0; i < binary.length; i++) {
            u8arr[i] = binary.charCodeAt(i);
        }
        
        let file = new File([u8arr], "image.jpeg", { type: mime });
        this.attachmentUploader.uploadFile(file);
        
        this.stopCamera();
        myModal.style.display = "none";
    },
    stopCamera: function() {
        let video = this.video.el;
        
        if (video.srcObject) {
            video.srcObject.getTracks().forEach(track => track.stop()); // Hentikan semua track kamera
            video.srcObject = null;
        }
    }
});
