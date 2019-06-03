# -*- coding: utf-8 -*-

# Scrapy settings for proxy project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'proxy'

SPIDER_MODULES = ['proxy.spiders']
NEWSPIDER_MODULE = 'proxy.spiders'

LOG_LEVEL = 'WARNING'
LOG_FILE = './log.log'

# DOWNLOAD_DELAY = 3
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
#    'proxy.middlewares.ProxySpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    'proxy.middlewares.ProxyDownloaderMiddleware': 543,
    # 'proxy.middlewares.RandomUserAgentMiddleware': 544,
    # 'proxy.middlewares.CheckUserAgentMiddleware': 545,
    'proxy.middlewares.ProxyMiddleware': 546,
    'proxy.middlewares.CheckProxyMiddleware': 547
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'proxy.pipelines.ProxyPipeline': 300,
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
MONGODB_DOCNAME = 'ipData'   # 西刺代理

PROXIES = [
    "http://39.137.107.98:80",
    "http://39.137.107.98:8080",
    "http://39.137.77.67:8080",
    "http://39.137.77.66:80",
    "http://39.137.77.66:8080",
    "http://111.206.6.101:80",
    "http://124.202.166.171:82",
    "http://117.191.11.104:8080",
    "http://117.191.11.106:80",
    "http://117.191.11.104:80",
    "http://117.191.11.103:80",
    "http://117.191.11.102:80",
    "http://117.191.11.103:8080",
    "http://117.191.11.107:8080",
    "http://117.191.11.72:8080",
    "http://117.191.11.106:8080",
    "http://117.191.11.105:80",
    "http://117.191.11.75:8080",
    "http://117.191.11.107:80",
    "http://117.191.11.101:80",
    "http://117.191.11.71:80",
    "http://117.191.11.72:80",
    "http://117.191.11.73:80",
    "http://117.191.11.71:8080",
    "http://117.191.11.74:8080",
    "http://117.191.11.73:8080",
    "http://117.191.11.75:80",
    "http://117.191.11.74:80",
    "http://117.191.11.101:8080",
    "http://117.191.11.102:8080",
    "http://117.191.11.105:8080",
    "http://101.251.215.232:8081",
    "http://68.183.99.96:8080",
    "http://120.210.219.104:80",
    "http://120.210.219.101:80",
    "http://120.210.219.102:80",
    "http://120.210.219.101:8080",
    "http://200.255.122.174:8080",
    "http://47.98.237.129:80",
    "http://47.107.233.107:80",
    "http://115.28.179.51:80",
    "http://39.137.77.68:8080",
    "http://39.137.77.67:80",
    "http://39.137.69.9:8080",
    "http://120.210.219.104:8080",
    "http://120.210.219.103:80",
    "http://121.8.98.196:80",
    "http://120.210.219.102:8080",
    "http://120.210.219.103:8080",
    "http://58.240.53.197:80",
    "http://39.137.69.8:80",
    "http://39.137.77.68:80",
    "http://39.137.69.8:8080",
    "http://134.209.73.47:8080",
    "http://159.89.141.36:8080",
    "http://157.230.13.186:8080",
    "http://142.93.196.92:8080",
    "http://13.56.2.56:8090",
    "http://162.211.126.220:443",
    "http://134.209.112.110:80",
    "http://157.230.57.151:8080",
    "http://157.230.227.116:80",
    "http://157.230.140.12:8080",
    "http://159.89.142.5:8080",
    "http://106.2.238.2:3128",
    "http://117.158.189.238:9999",
    "http://118.190.145.138:9001",
    "http://113.53.230.167:80",
    "http://68.183.53.127:8080",
    "http://68.183.156.72:80",
    "http://159.89.35.245:8080",
    "http://185.34.52.82:80",
    "http://134.209.112.110:3128",
    "http://85.43.127.116:80",
    "http://142.4.204.85:8080",
    "http://157.230.212.164:8080",
    "http://206.189.95.220:80",
    "http://138.219.228.122:8080",
    "http://192.33.31.130:80",
    "http://121.40.138.161:8000",
    "http://207.180.226.111:80",
    "http://51.77.162.148:3128",
    "http://218.60.8.98:3129",
    "http://104.248.8.35:8080",
    "http://218.60.8.99:3129",
    "http://111.230.113.238:9999",
    "http://164.125.68.172:9999",
    "http://157.230.57.151:80",
    "http://218.60.8.83:3129",
    "http://223.96.95.229:3128",
    "http://65.52.174.40:80",
    "http://211.103.153.29:3128",
    "http://39.96.210.247:80",
    "http://121.12.85.2:80",
    "http://207.180.226.111:8080",
    "http://210.34.24.103:3128",
    "http://39.137.69.9:80",
    "http://103.249.182.15:80",
]

SCHEDULER = "scrapy_redis.scheduler.Scheduler"
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
SCHEDULER_PERSIST = True