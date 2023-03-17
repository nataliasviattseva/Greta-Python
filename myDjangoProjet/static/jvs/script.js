const COURRIEL = "contact@greta-yvelines.fr";

function checkSubmit(){
    inputText = document.forms["mailForm"].element["mailInput"].value;
        if(inputText == COURRIEL){
            document.getElementById("checkSpan").innerText = "OK";
//            document.getElementById("mailForm").submit();
        } else {
            document.getElementById("checkSpan").innerText = "! Courriel Incorrect !";
            document.getElementById("mailInput").value = "";
            document.getElementById("mailInput").focus();
        }
}

function getImgWidth(img){
    alert("image width : " + img.width);
}

function setDivWidth(){
    var imgWidth = document.getElementById("imgGreta78").width;
//    document.getElementById("divFormationDjango").style.width = imgWidth + "px"
}

function setSectionPosition(){
    var bodyHeight = document.body.clientHeight;
    document.getElementById("passSection").style.marginTop = (bodyHeight/4) + "px";
}
