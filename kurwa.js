const urlList = [
  {
    loc: 'https://freevpnplanet.com/',
  },
  {
    loc: 'https://freevpnplanet.com/download/',
  },
  {
    loc: 'https://freevpnplanet.com/ar/',
  },
  {
    loc: 'https://freevpnplanet.com/ar/download/',
  },
  {
    loc: 'https://freevpnplanet.com/de/',
  },
  {
    loc: 'https://freevpnplanet.com/de/download/',
  },
  {
    loc: 'https://freevpnplanet.com/es/',
  },
  {
    loc: 'https://freevpnplanet.com/es/download/',
  },
  {
    loc: 'https://freevpnplanet.com/fr/',
  },
  {
    loc: 'https://freevpnplanet.com/fr/download/',
  },
];

const group_links = (urlList) => {
  const result = urlList.reduce((accumulator, current) => {
    const match = current.loc.match(/\/([a-z]{2})\//);
    const lang = match && match[1] ? match[1] : 'en';
    let page = '';
    if (match && current.loc.split('/')[4]) {
      page = current.loc.split('/')[4];
    } else if (!match && current.loc.split('/')[3]) {
      page = current.loc.split('/')[3];
    } else {
      page = 'base url';
    }

    if (!accumulator[lang]) {
      accumulator[lang] = {};
    }
    accumulator[lang][page] = current.loc;
    return accumulator;
  }, {});

  return result;
};

console.log(group_links(urlList));
