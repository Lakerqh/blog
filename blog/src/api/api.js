let _api = '/api';
let api = {
    login: _api + '/admin/login',  //登录
    register: _api + '/admin/register', //注册
    registeReader: _api + '/admin/registeReader', //读者注册
    check: _api + '/admin/check',  //审核注册账号
    getmenu: _api + '/admin/getmenu', //获取从系统菜单
}

export default api;