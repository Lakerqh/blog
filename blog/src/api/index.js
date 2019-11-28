import axios from 'axios';
// import qs from 'qs';
// axios.defaults.headers.post['Content-Type'] = 'application/x-www-form-urlencoded';

// 添加请求拦截器
axios.interceptors.request.use(function (config) {
    // 添加headers到post请求中
    // config.headers.post['Content-Type'] = 'application/json;charset=utf-8';
    // let userInfo = localStorage.getItem('userInfo');
    // if (userInfo != null) {
    //     config.headers['sid'] = JSON.parse(userInfo).sid;
    //     config.headers['userNo'] = JSON.parse(userInfo).userNo;
    // }
    return config;
}, function (error) {
    return Promise.reject(error);
});

// 添加响应拦截器
axios.interceptors.response.use(function (response) {
    return response;
}, function (error) {
    // 对响应错误做点什么
    return Promise.reject(error);
});

export const http = {
    get(url) {
        return new Promise((resolve, reject) => {
            axios.get(url).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    delete(url, params) {
        return new Promise((resolve, reject) => {
            axios.delete(url, params).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    post(url, params) {
        return new Promise((resolve, reject) => {
            axios.post(url, params).then((response) => {
                resolve(response);
            }).catch((error) => {
                reject(error)
            })
        })
    },
    put(url, params) {
        return new Promise((resolve, reject) => {
            axios.put(url, params).then(function (data) {
                resolve(data);
            }).catch((error) => {
                reject(error)
            })
        })
    },
}
