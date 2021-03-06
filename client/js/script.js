// fullscreen js
var elem = document.documentElement;
var fullscreenOpen = false;
var submissionString = {};


function toggleFullscreen() {
    var iconPath = ""
    // console.log(fullscreenOpen);
    if (fullscreenOpen) {
        fullscreenOpen = false;
        document.getElementById('fullscreen-button').src = "./assets/imgs/open.svg";
        return closeFullscreen();
    } else {
        fullscreenOpen = true;
        document.getElementById('fullscreen-button').src = "./assets/imgs/close.svg";
        return openFullscreen();
    }
}

function openFullscreen() {
    if (elem.requestFullscreen) {
        elem.requestFullscreen();
    } else if (elem.webkitRequestFullscreen) { /* Safari */
        elem.webkitRequestFullscreen();
    } else if (elem.msRequestFullscreen) { /* IE11 */
        elem.msRequestFullscreen();
    }
}

function closeFullscreen() {
    if (document.exitFullscreen) {
        document.exitFullscreen();
    } else if (document.webkitExitFullscreen) { /* Safari */
        document.webkitExitFullscreen();
    } else if (document.msExitFullscreen) { /* IE11 */
        document.msExitFullscreen();
    }
}

// save to textarea content to txt file
function saveToText() {
    var text = document.getElementById("text-area").value;
    alert(text);
}

function addq1() {
    submissionString["q1"] = document.getElementById("text-area").value;
    console.log(submissionString)
    $.ajax({
        url: "http://127.0.0.1:5000/submit_journal_text_partial", 
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(submissionString),
        success: function( data ) { 
            document.getElementById('save-button').remove();
        }   
    });
}

function addq2AndPost() {
    submissionString["q2"] = document.getElementById("text-area").value;
    console.log(submissionString)
    $.ajax({
        url: "http://127.0.0.1:5000/submit_journal_text", 
        type: "POST",
        contentType: "application/json",
        data: JSON.stringify(submissionString),
        success: function( data ) { 
            document.getElementById('save-button').remove();
        }   
    });
}