import scrapy

class VideoSpider(scrapy.Spider):
    name = "video_spider"
    allowed_domains = ["xnxx.com"]
    start_urls = [
        'https://www.xnxx.com/best-of-trans/2024-09'  # Replace with the actual URL to scrape
    ]

    def parse(self, response):
        # Extracting all video elements
        for video in response.css('div.thumb-block'):
            video_page = video.css('a::attr(href)').get()
            thumbnail = video.css('img::attr(src)').get()
            title = video.css('a::text').get()  # Extracting the title text

            # Form the complete URL for each video page
            video_page_url = response.urljoin(video_page)

            # Yield video information if available
            if video_page_url and thumbnail:
                yield {
                    'title': title if title else 'No title',
                    'thumbnail': thumbnail,
                    'video_page_url': video_page_url
                }

        # Follow pagination links, if available
        next_page = response.css('a.next::attr(href)').get()
        if next_page:
            yield response.follow(next_page, self.parse)
