import re
import xml.etree.ElementTree as ET
import requests
from pprint import pprint



class SiteMap:
    FEEVPN_SITEMAP_URL = "https://freevpnplanet.com/sitemap.xml"
    XMLNS = "{http://www.sitemaps.org/schemas/sitemap/0.9}"

    @staticmethod
    def get():
        """
        The `get` method retrieves URLs from an XML sitemap and groups them.

        Return:
            The `get` method is returning the result of calling the `group_links` method on the list of
            URLs extracted from the XML data.
        """
        freevpn_sitemap = SiteMap.get_urls_list(SiteMap.FEEVPN_SITEMAP_URL)

        return SiteMap.group_links(freevpn_sitemap)

    @staticmethod
    def get_urls_list(url: str) -> list:
      response = requests.get(url)
      xml_data = response.content
      root = ET.fromstring(xml_data)
      urls = []

      # Iterate over all <url> elements in the XML tree
      for url in root.findall(f"{SiteMap.XMLNS}url"):
          # Find the <loc> element in each <url> element and get its text
          loc_element = url.find(f"{SiteMap.XMLNS}loc")
          loc_text = loc_element.text if loc_element is not None else None
          urls.append(loc_text)

      return urls
       

    @staticmethod
    def group_links(urls: list) -> dict:
        """Groups URLs by language and page within the list.

        Args:
            urls: A list of strings(url)

        Return:
            A dictionary where keys are languages (extracted from the URL)
            and values are dictionaries where keys are pages (extracted from the URL)
            and values are the corresponding URLs from the input list.
        """
        result = {}
        for url in urls:
            print(url.split("/"))
            match = re.search(r"\/([a-z]{2})\/", url)
            lang = (
                match.group(1) if match else "en"
            )  # Default to 'en' if no language match

            page = ""
            url_parts = url.split("/")
            if match and url_parts[4]:
                page = url_parts[4] if not url_parts[5] else '/'.join([url_parts[4],url_parts[5]])
            elif not match and url_parts[3]:
                page = url_parts[3] if not url_parts[4] else '/'.join([url_parts[3],url_parts[4]])

            if page == "":
                page = "base url"  # Set page to 'base url' if no page extracted

            result.setdefault(lang, {}).setdefault(page, url)

        return result


sitemap_links = SiteMap.get()



