chrome.runtime.sendMessage({action: 'extractText', data: {title: document.title, url: window.location.href, content: document.body.innerText}});