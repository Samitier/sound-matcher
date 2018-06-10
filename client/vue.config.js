module.exports = {
	outputDir: '../soundmatcher/static',
	devServer: {
		proxy: 'http://localhost:8000'
	},
	baseUrl: process.env.NODE_ENV === 'production'
		? '/static/'
		: '/'
}