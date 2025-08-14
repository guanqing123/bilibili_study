function n(t) {
    return new Md5(!0).update(t)[e]()
}

i = function(e, t, c, a) {
    var s = e.indexOf("?");
    s > 0 && (e = e.substring(0, s));
    var i = e + JSON.stringify(t) + c;
    return a && (i += a),
    i
}