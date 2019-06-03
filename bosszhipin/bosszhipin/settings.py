# -*- coding: utf-8 -*-

# Scrapy settings for bosszhipin project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'bosszhipin'

SPIDER_MODULES = ['bosszhipin.spiders']
NEWSPIDER_MODULE = 'bosszhipin.spiders'

LOG_LEVEL = 'WARNING'
LOG_FILE = './log.log'

DOWNLOAD_DELAY = 3
COOKIES_ENABLES = False

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.157 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'bosszhipin.middlewares.BosszhipinSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'bosszhipin.middlewares.BosszhipinDownloaderMiddleware': 543,
    # 'bosszhipin.middlewares.RandomUserAgentMiddleware': 544,
    # 'bosszhipin.middlewares.CheckUserAgentMiddleware': 545,
    'bosszhipin.middlewares.ProxyMiddleware': 546,
    'bosszhipin.middlewares.CheckProxyMiddleware': 547
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'bosszhipin.pipelines.BosszhipinPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

USER_AGENT_LIST = [
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; AcooBrowser; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)",
    "Mozilla/4.0 (compatible; MSIE 7.0; AOL 9.5; AOLBuild 4337.35; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",
    "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
    "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20",
    "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36",
    "Dalvik/1.6.0 (Linux; U; Android 4.2.1; 2013022 MIUI/JHACNBL30.0)",
    "Mozilla/5.0 (Linux; U; Android 4.4.2; zh-cn; HUAWEI MT7-TL00 Build/HuaweiMT7-TL00) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "AndroidDownloadManager",
    "Apache-HttpClient/UNAVAILABLE (java 1.4)",
    "Dalvik/1.6.0 (Linux; U; Android 4.3; SM-N7508V Build/JLS36C)",
    "Android50-AndroidPhone-8000-76-0-Statistics-wifi",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.4; MI 3 MIUI/V7.2.1.0.KXCCNDA)",
    "Dalvik/1.6.0 (Linux; U; Android 4.4.2; Lenovo A3800-d Build/LenovoA3800-d)",
    "Lite 1.0 ( http://litesuits.com )",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.122 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/5.0 (Linux; U; Android 4.1.1; zh-cn; HTC T528t Build/JRO03H) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30; 360browser(securitypay,securityinstalled); 360(android,uppayplugin); 360 Aphone Browser (2.0.4)",
]

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'MySpider'
MONGODB_DOCNAME = 'Boss'   # Boss直聘

PROXIES = [
    "https://120.234.63.196:3128",
    "http://117.191.11.78:8080",
    "https://94.191.40.157:8118",
    "http://123.245.12.54:8118",
    "http://112.247.182.111:8060",
    "http://210.61.46.165:3128",
    "http://183.233.90.6:8080",
    "https://118.24.151.76:8118",
    "http://116.62.215.123:8118",
    "http://117.191.11.102:80",
    "https://47.98.219.151:8888",
    "https://47.89.37.177:3128",
    "http://117.191.11.80:80",
    "http://150.138.117.24:1080",
    "http://111.206.6.101:80",
    "http://112.247.182.111:8060",
    "http://106.75.212.158:8080",
    "http://188.131.185.226:1081",
    "http://129.211.18.237:1081",
    "http://121.226.61.155:8118",
    "http://117.191.11.73:80",
    "https://123.163.97.113:9999",
    "https://61.128.208.94:3128",
    "https://60.10.22.229:63141",
    "http://39.137.77.66:8080",
    "http://117.191.11.102:80",
    "http://117.191.11.105:80",
    "http://117.191.11.79:80",
    "http://148.70.80.214:1080",
    "http://111.231.22.98:1080",
    "https://111.26.9.26:80",
    "http://120.210.219.103:8080",
    "http://47.91.243.86:83",
    "https://112.109.198.106:3128",
    "http://47.99.103.219:1080",
    "http://47.99.110.148:1080",
    "http://111.226.211.73:8118",
    "https://39.98.189.213:8888",
    "http://36.40.86.22:1080",
    "http://150.138.114.9:1080",
    "http://119.28.31.29:8888",
    "http://122.152.227.117:1080",
    "https://123.206.30.254:8118",
    "https://118.89.44.224:8118",
    "http://47.97.82.218:8080",
    "http://202.109.157.67:9000",
    "http://39.106.16.111:80",
    "http://111.231.87.160:8088",
    "https://119.28.85.72:8118",
    "http://117.191.11.78:8080",
    "http://118.24.145.90:1080",
    "http://212.64.87.146:1080",
    "https://221.7.255.168:80",
    "https://47.93.28.220:8118",
    "https://129.204.12.208:8000",
    "http://117.191.11.75:8080",
    "http://117.191.11.103:80",
    "http://58.176.13.2:80",
    "http://47.94.213.22:8888",
    "https://112.85.170.119:9999",
    "http://118.190.95.35:9001",
    "http://211.23.25.207:443",
    "http://123.206.133.124:1080",
    "http://123.144.201.154:8118",
    "http://132.232.129.206:1080",
    "http://101.4.136.34:81",
    "http://117.191.11.72:80",
    "http://193.112.12.33:1081",
    "http://118.190.94.224:9001",
    "https://106.12.124.116:8118",
    "https://111.230.167.207:8118",
    "http://122.137.4.105:8080",
    "http://152.136.52.212:1081",
    "https://94.191.40.157:8118",
    "http://121.41.17.181:1080",
    "http://39.137.69.10:8080",
    "http://111.231.7.214:1080",
    "http://117.191.11.113:80",
    "http://117.191.11.76:80",
    "https://119.23.105.110:8118",
    "http://152.136.150.67:1081",
    "http://152.136.14.27:8888",
    "http://223.19.212.30:8380",
    "http://117.191.11.103:8080",
    "https://111.230.254.195:8118",
    "http://182.138.153.213:8118",
    "https://111.197.236.117:9999",
    "http://129.28.81.148:1080",
    "http://124.156.183.171:808",
    "http://27.208.184.76:8060",
    "https://43.255.228.150:3128",
    "http://202.109.157.62:9000",
    "https://47.104.157.189:8118",
    "http://42.51.196.8:808",
    "http://119.180.168.79:8060",
    "http://129.211.2.62:1081",
    "http://223.19.212.30:80",
    "http://113.252.222.73:8197",
    "https://47.52.69.253:3128",
]