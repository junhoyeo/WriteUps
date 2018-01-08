
function processShortcut(event) {
	if (T.config.PREVIEW) {
		return;
	}

	if (isIE)
	{
		event = window.event;
		event.target = event.srcElement;
	}

	if (event.altKey || event.ctrlKey || event.metaKey)
		return;
	switch (event.target.nodeName) {
		case "INPUT":
		case "SELECT":
		case "TEXTAREA":
			return;
	}
	switch (event.keyCode) {
		case 81: //Q
			if (T.config.ROLE == 'user') {
				permissionNotice();
			} else {
				window.location = TistoryBlog.tistoryUrl + "/manage";
			}
			break;

		case 65: //A
			if (T.config.PREV_PAGE) {
				window.location = T.config.PREV_PAGE;
			}
			break;

		case 83: //S
			if (T.config.NEXT_PAGE) {
				window.location = T.config.NEXT_PAGE;
			}
			break;

		case 90: //Z
			window.location = "#recentEntries";
			break;

		case 88: //X
			window.location = "#recentComments";
			break;

	}
}
document.onkeydown = processShortcut;

function addComment(caller, entryId) {
	var oForm = findFormObject(caller);
	if (!oForm)
		return false;
	var request = new HTTPRequest("POST", oForm.action);
	request.onSuccess = function () {
		if(entryId == 0)
			window.location = blogURL + "/guestbook";
		else {
			document.getElementById("entry" + entryId + "Comment").innerHTML = this.getText("/response/commentBlock");
			if(document.getElementById("recentComments"))
				document.getElementById("recentComments").innerHTML = this.getText("/response/recentCommentBlock");
			if(document.getElementById("commentCount" + entryId))
				document.getElementById("commentCount" + entryId).innerHTML = this.getText("/response/commentView");
			if(document.getElementById("commentCountOnRecentEntries" + entryId))
				document.getElementById("commentCountOnRecentEntries" + entryId).innerHTML = "(" + this.getText("/response/commentCount") + ")";
		}
		if(typeof window.needCommentCaptcha !== "undefined"){
			captchaPlugin.init('complete');
		}
	}
	request.onError = function() {
		var description = this.getText("/response/description");
		if (description) { alert(description); }
	}
	var queryString = "key=tistory";
	var captchaInput = document.getElementById('inputCaptcha');
	if (oForm["name"])
		queryString += "&name=" + encodeURIComponent(oForm["name"].value);
	if (oForm["password"]) {
		var passwd = oForm["password"].value.trim();
		if (passwd.length > 0) {
			var shaObj = new jsSHA("SHA-256", "TEXT");
			shaObj.update(md5(encodeURIComponent(passwd)));
			queryString += "&password=" + shaObj.getHash("HEX");
		} else {
			alert('비밀번호를 넣어주세요.');
			return false;
		}
	}
	if (oForm["homepage"])
		queryString += "&homepage=" + encodeURIComponent(oForm["homepage"].value);
	if (oForm["secret"] && oForm["secret"].checked)
		queryString += "&secret=1";
	if (oForm["comment"])
		queryString += "&comment=" + encodeURIComponent(oForm["comment"].value);
	if (captchaInput) {
		if (!captchaInput.value) {
			alert('그림문자가 입력되지 않았습니다.');
			return false;
		}
		queryString += "&captcha=" + encodeURIComponent(captchaInput.value);
	}
	request.send(queryString);
}


function commentRequireLogin() {
	if(confirm(T.config.COMMENT_LOGIN_CONFIRM_MESSAGE)) {
		window.location = T.config.LOGIN_URL;
	} else {
		window.focus();
	}
}

function commentObserverForAuth(evetObj) {
	var reex = /name|password|homepage|secret|comment/,
		name;
	if (isIE) {
		name = evetObj.srcElement.name;
	} else {
		name = evetObj.target.name;
	}
	if (reex.test(name) && !(new RegExp("^entry\\d+password$").test(name))) {
		commentRequireLogin();
	}
}


if (T.config.NEED_COMMENT_LOGIN && T.config.ROLE == 'GUEST') {
	STD.addEventListener(document);
	document.addEventListener("click", commentObserverForAuth, false);
}


function commentVisibility(id) {
	var visibility = document.getElementById('commentVisibility_'+id);
	if(visibility.innerHTML == "[승인완료]")
		return false;
	var request = new HTTPRequest("POST", "/admin/comment/approve.php");
	visibility.innerHTML = "[승인중]";
	request.onVerify = function() {
		try {
			var result = eval("(" + this.getText() + ")");
			return (result.error == false)
		}
		catch (e) {
			return false;
		}
	};
	request.onSuccess = function() {
		document.getElementById('commentVisibility_'+id).innerHTML = "[승인완료]"
	};
	request.onError = function() {
		document.getElementById('commentVisibility_'+id).innerHTML = "[승인실패]"
	};
	request.send('id=' + id + '&approved=1');
}

var openWindow='';
function alignCenter(win,width,height) {
	if(navigator.userAgent.indexOf("Chrome") == -1)
		win.moveTo(screen.width/2-width/2,screen.height/2-height/2);
}

function deleteComment(id) {
	var width = 450;
	var height = 550;
	try { openWindow.close(); } catch(e) { }
	openWindow = window.open("/comment/manage/" + id, "tatter", "width="+width+",height="+height+",location=0,menubar=0,resizable=0,scrollbars=0,status=0,toolbar=0");
	openWindow.focus();
	alignCenter(openWindow,width,height);
}

function deleteGuestbookComment(id, guestbookWrittenPage) {
    var width = 450;
    var height = 550;
    try { openWindow.close(); } catch(e) { }
    openWindow = window.open("/comment/manage/" + id + (guestbookWrittenPage ? "?guestbookWrittenPage=" + guestbookWrittenPage: ""), "tatter", "width="+width+",height="+height+",location=0,menubar=0,resizable=0,scrollbars=0,status=0,toolbar=0");
    openWindow.focus();
    alignCenter(openWindow,width,height);
}

function commentComment(parent) {
    var visibility = document.getElementById('commentVisibility_'+parent);
    if(visibility === null || visibility.innerHTML == "[승인완료]") {
        var width = 450;
        var height = 550;
        try {
            openWindow.close();
        } catch (e) {
        }
        openWindow = window.open("/comment/comment/" + parent, "tatter", "width=" + width + ",height=" + height + ",location=0,menubar=0,resizable=0,scrollbars=0,status=0,toolbar=0");
        openWindow.focus();
        alignCenter(openWindow, width, height);
    }
    else {
        alert('승인 대기중인 댓글에는 답글을 작성할 수 없습니다.');
        return false;
	}
}

function guestbookCommentComment(parent, guestbookWrittenPage) {
    var visibility = document.getElementById('commentVisibility_'+parent);
    if(visibility === null || visibility.innerHTML == "[승인완료]") {
        var width = 450;
        var height = 550;
        try {
            openWindow.close();
        } catch (e) {
        }
        openWindow = window.open("/comment/comment/" + parent + (guestbookWrittenPage ? "?guestbookWrittenPage=" + guestbookWrittenPage : ""), "tatter", "width=" + width + ",height=" + height + ",location=0,menubar=0,resizable=0,scrollbars=0,status=0,toolbar=0");
        openWindow.focus();
        alignCenter(openWindow, width, height);
    }
    else {
        alert('승인 대기중인 댓글에는 답글을 작성할 수 없습니다.');
        return false;
    }
}

function editEntry(parent) {
	var apiFrame = document.getElementById('editEntry');
	apiFrame.contentWindow.postMessage(parent, TistoryBlog.tistoryUrl);
}

window.addEventListener('message', function(event) {
	if (event.origin !== TistoryBlog.tistoryUrl) {
		return;
	}

	if (event.data === 'reload') {
		window.document.location.reload()
	}
}, false);

function guestbookComment(parent) {
	var width = 450;
	var height = 550;
	try { openWindow.close(); } catch(e) { }
	openWindow = window.open("/comment/comment/" + parent, "tatter", "width="+width+",height="+height+",location=0,menubar=0,resizable=0,scrollbars=0,status=0,toolbar=0");
	openWindow.focus();
	alignCenter(openWindow,width,height);
}

function deleteTrackback(id, entryId) {
	if (T.config.ROLE != 'MEMBER' && T.config.ROLE != "owner") {
		if (confirm("트랙백을 삭제하기 위해서는 로그인이 필요합니다.\n로그인 하시겠습니까?")) {
			window.location = T.config.LOGIN_URL;
		}
		return false;
	}

	if (!confirm("선택된 트랙백을 삭제합니다. 계속하시겠습니까?"))
		return;

	var request = new HTTPRequest("GET", "/trackback/delete/" + id);
	request.onSuccess = function() {
		var target = document.getElementById('trackback'+id);
		if (target) {
			target.parentNode.removeChild(target);
		}
		if(document.getElementById("recentTrackbacks")) {
			document.getElementById("recentTrackbacks").innerHTML = this.getText("/response/recentTrackbackBlock");
		}
		if(document.getElementById("trackbackCount" + entryId)) {
			document.getElementById("trackbackCount" + entryId).innerHTML = this.getText("/response/trackbackView");
		}
	};
	request.onError = function() {
		alert(this.getText("/response/result"));
	};
	request.send();

}

function changeVisibility(id, visibility) {
	var request = new HTTPRequest("POST", "/admin/entry/setVisibility.php");
	request.onVerify = function() {
		try {
			var result = eval("(" + this.getText() + ")");
			if(result.data.event == 'join'){
				alert("이벤트에 참여한 글은 공개설정을 변경하실 수 없습니다.");
				return false;
			} else {
				return (result.error == false)
			}
		}
		catch (e) {
			return false;
		}
	};
	request.onSuccess = function() {
		window.location.reload();
	};
	request.send("ids=" + id + "&visibility=" + visibility);
}

function deleteEntry(id) {
	if (!confirm("이 글 및 이미지 파일을 완전히 삭제합니다. 계속하시겠습니까?")) {
		return;
	}
	var request = new HTTPRequest("POST", "/admin/entry/delete/");
	request.onSuccess = function() {
		window.location.reload();
	};
	request.onError = function () {
		alert('삭제에 실패 했습니다');
	};
	request.send("ids="+id);
}

function reloadEntry(id) {
	var password = document.getElementById("entry" + id + "password");
	if (!password)
		return;
	document.cookie = "GUEST_PASSWORD=" + encodeURIComponent(password.value) + ";path=";

	window.location.reload();
}

function permissionNotice(oEvent){
	if(confirm(T.config.USER.name + '님의 블로그가 아닙니다. ' + T.config.USER.homepage + '의 관리자로 이동 하시겠습니까?')){
		document.location.href = T.config.USER.homepage + '/manage';
	}
	try {
		oEvent.preventDefault();
	} catch(e) {
		event.returnValue = false;
		event.cancelBubble = true;
	}
}

loadedComments = new Array();
loadedTrackbacks = new Array();
function viewTrigger(id, category, categoryId) {
	var request = new HTTPRequest("GET", "/"+category+"/view/" + id);
	var target = document.getElementById('entry'+id+(category == 'comment' ? 'Comment' : 'Trackback'));
	if(target == null)
		return false;
	request.onSuccess = function() {
		target.innerHTML = this.getText("/response/result");
		target.style.display = 'block';
		category == 'comment' ? loadedComments[id] = true : loadedTrackbacks[id] = true;
		if(categoryId > -1)
			location = location.toString();
		if(typeof window.needCommentCaptcha !== "undefined"){
			captchaPlugin.init();
		}
        findFragmentAndHighlight();
	};
	request.onError = function() {
		alert('실패 했습니다');
	};
	request.send();
}
function highlight() {
	var hash = new RegExp("^#(comment\\d+)").exec(window.location.hash);
	if(hash && (el = document.getElementById(hash[1])))
		highlightElement(hash[1], 0, el.style.backgroundColor);
}
function highlightElement(id, amount, origColor) {
	var el = document.getElementById(id);
	if (!el) {
		return;
	}
	el.style.backgroundColor = amount % 2 ? "#FFFF44" : origColor;
	if (++amount < 7) {
		setTimeout("highlightElement('" + id + "', " + amount + ", '" + origColor + "')", 200);
	}
}
function toggleLayerForEntry(id, category, categoryId, mode) {
	if((category == 'comment' ? loadedComments[id] : loadedTrackbacks[id])) {
		try {
			var obj = document.getElementById('entry'+id+(category == 'comment' ? 'Comment' : 'Trackback'));
			if(mode == undefined)
				obj.style.display = (obj.style.display == "none") ? "block" : "none";
			else
				obj.style.display = (mode == 'show') ? "block" : "none";
		} catch (e) {

		}
		return true;
	} else {
		if(categoryId) {
			viewTrigger(id,category, categoryId);
		} else {
			viewTrigger(id,category, -1);
		}
	}
}
function ObserverForAnchor(evetObj) {
	var lo = location.toString();
	var queryString = lo.substr(lo.lastIndexOf('/')+1);
	if(queryString.indexOf('#')>-1) {
		var qsElements = queryString.split('#');
		if(qsElements[1].indexOf('comment')>-1) {
			var category = 'comment';
		} else if(qsElements[1].indexOf('trackback')>-1) {
			var category = 'trackback';
		}
		if(category) {
			entryid = qsElements[0];
			categoryId = qsElements[1].substr(category.length);
			toggleLayerForEntry(entryid,category,categoryId, 'show');
		}
	}
}

STD.addEventListener(window);
window.addEventListener("load", ObserverForAnchor, false);


function secondaryDomainLogin(authData) {
	if (!authData) {
		return;
	}

	var request = new HTTPRequest("POST", '/api/secondaryDomain/');
	request.async = false;
	request.onSuccess = function() {
		window.location.reload();
	};
	request.onVerify = function() {
		try {
			var result = eval("(" + this.getText() + ")");
			return (result.error == false)
		}
		catch (e) {
			return false;
		}
	};
	request.send('authData=' + encodeURIComponent(authData));
}
