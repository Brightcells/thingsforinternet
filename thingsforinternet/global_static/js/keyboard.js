//localstorage降级处理
if (!window.localStorage) {
  window.localStorage = {
      getItem: function (sKey) {
          if (!sKey || !this.hasOwnProperty(sKey)) return null
          return unescape(document.cookie.replace(new RegExp("(?:^|.*;\\s*)" + escape(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=\\s*((?:[^;](?!;))*[^;]?).*"), "$1"))
      },
      key: function (nKeyId) {
          return unescape(document.cookie.replace(/\s*\=(?:.(?!;))*$/, "").split(/\s*\=(?:[^;](?!;))*[^;]?;\s*/)[nKeyId])
      },
      setItem: function (sKey, sValue) {
          if(!sKey) return
          document.cookie = escape(sKey) + "=" + escape(sValue) + "; expires=Tue, 19 Jan 2038 03:14:07 GMT; path=/"
          this.length = document.cookie.match(/\=/g).length
      },
      length: 0,
      removeItem: function (sKey) {
          if (!sKey || !this.hasOwnProperty(sKey)) return
          document.cookie = escape(sKey) + "=; expires=Thu, 01 Jan 1970 00:00:00 GMT; path=/"
          this.length--
      },
      hasOwnProperty: function (sKey) {
          return (new RegExp("(?:^|;\\s*)" + escape(sKey).replace(/[\-\.\+\*]/g, "\\$&") + "\\s*\\=")).test(document.cookie)
      }
  }
  window.localStorage.length = (document.cookie.match(/\=/g) || window.localStorage).length
}

//默认
if ( 'OVER' != getCookie("FIRSTTIME") ) {
    setCookie("_B", "http://www.baidu.com")
    setCookie("_G", "http://www.google.com")
    setCookie("_V", "http://www.v2ex.com")
    setCookie("_W", "http://www.weibo.com")
    setCookie("_Y", "https://www.youtube.com/")
    setCookie("FIRSTTIME", "OVER")
}

var urlcache = {}

for (var i = 48; i <= 90; i++) {
    var code = String.fromCharCode(i)
    var v = getCookie("_" + code)

    if (v != null && v != '' && typeof(v) != 'undefined') {
        urlcache[code] = v
        $("#LI_" + code).prepend('<img id="' + code + '" class="fav" src="' + getico(v) + '" align="center">')
    }
}
 
$(document).keyup(function(ev) {
    if (ev.ctrlKey) return false
    var code = String.fromCharCode(ev.keyCode)
    $("#LI_" + code).addClass("active")
    setTimeout('$("#LI_' + code + '").removeClass("active");', 300)
    if (urlcache[code] == '' || typeof(urlcache[code]) == 'undefined') {
        $("#message").html('找不到这个按键的配置,注意切换您的输入法哦~~~')
        setTimeout('$("#message").html("");', 2000)
    } else window.open(urlcache[code])
})

$("#main li").mouseenter(function() {
    $("#tempdate").val($(this).attr('id').replace("LI_", ""))
    $(this).append('<div class="oper"><span><a onclick="return del()" class="del" title="删除"><img src="/static/img/delete-icon.png"></a></span><span><a onclick="return update()" class="edit" title="编辑"><img src="/static/img/edit-icon.png"></a></span></div>')
}).mouseleave(function() {
    $("#tempdate").val('')
    $(".oper").remove()
})

$("#main li").click(function() {
    var code = $(this).attr('id').replace('LI_', '')
    if (urlcache[code] != '' && typeof(urlcache[code]) != 'undefined') {
        window.open(urlcache[code])
    }
})

function del() {
    var code = $("#tempdate").val()
    urlcache[code] = ''
    $("#" + code).remove()
    deleteCookie("_" + code)
    return false
}

function update() {
    var code = $("#tempdate").val()
    $("#LI_" + code).css('background', '#ccf')
    var u = window.prompt("请输入键位 [" + code + "] 对应的网站地址", "")
    $("#LI_" + code).css('background', '#fff')
    if (u.indexOf('http://') == -1 && u.indexOf('https://') == -1) {
        u = 'http://' + u
    }
    if (!IsURL(u)) {
        alert('网站地址输入错误!请核对')
        return false
    }
    urlcache[code] = u
    $("#" + code).remove()
    $("#LI_" + code).prepend('<img id="' + code + '" class="fav" src="' + getico(u) + '" align="center">')
    setCookie("_" + code, u)
    return true
};

function getico(url) {
    var s = url.indexOf("//")
    temp = url.substring(s + 2)
    var s1 = temp.indexOf("/")
    if (s1 == -1) {
        s1 = temp.length
    }
    return url.substring(0, s1 + s + 2) + '/favicon.ico'
}

function setCookie(name, value, path, domain, secure) {
    localStorage.setItem(name, value)
}

function deleteCookie(name) {
    localStorage.removeItem(name)
}

function getCookie(name) {
    return  localStorage.getItem(name)
}

function IsURL(str_url) {
    var strRegex = "^((https|http|ftp|rtsp|mms)?://)" + "?(([0-9a-z_!~*'().&=+$%-]+: )?[0-9a-z_!~*'().&=+$%-]+@)?" + "(([0-9]{1,3}.){3}[0-9]{1,3}" + "|" + "([0-9a-z_!~*'()-]+.)*" + "([0-9a-z][0-9a-z-]{0,61})?[0-9a-z]." + "[a-z]{2,6})" + "(:[0-9]{1,4})?" + "((/?)|" + "(/[0-9a-z_!~*'().;?:@&=+$,%#-]+)+/?)$"
    var re = new RegExp(strRegex)
    return !!re.test(str_url)
}
