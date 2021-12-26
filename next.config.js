const withNextra = require('nextra')('nextra-theme-blog', './theme.config.js')
module.exports = withNextra({
    images:{
        domains: ['seongwoon-blog.s3.ap-northeast-2.amazonaws.com']
    },
})
