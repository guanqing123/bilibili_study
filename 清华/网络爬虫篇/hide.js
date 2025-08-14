// hide.js - 隐藏 Selenium WebDriver 自动化特征
// 使用方法：通过 execute_cdp_cmd 或 --js-flags 注入执行

// 1. 删除 navigator.webdriver 属性
Object.defineProperty(navigator, 'webdriver', {
  get: () => undefined,
  enumerable: false,
  configurable: true
});

// 2. 修改 navigator 相关属性（常见检测点）
Object.defineProperty(navigator, 'languages', {
  get: () => ['zh-CN', 'zh', 'en'],
  enumerable: true
});

Object.defineProperty(navigator, 'plugins', {
  get: () => [1, 2, 3],
  enumerable: true
});

// 3. 覆盖 window.chrome 属性
window.chrome = {
  runtime: {},
  // 添加其他常见 chrome 属性
  app: {
    isInstalled: false
  }
};

// 4. 隐藏 Permissions API 的自动化特征
if (window.Notification) {
  Object.defineProperty(Notification, 'permission', {
    get: () => 'default',
    enumerable: true
  });
}

// 5. 覆盖 WebDriver 相关方法
if (window.document.$cdc_asdjflasutopfhvcZLmcfl_ || window.document.__driver_evaluate) {
  delete window.document.$cdc_asdjflasutopfhvcZLmcfl_;
  delete window.document.__driver_evaluate;
}

// 6. 修改屏幕分辨率相关属性（可选）
Object.defineProperty(screen, 'width', {
  get: () => window.screen.width,
  enumerable: true
});

// 7. 阻止 WebRTC 泄漏真实 IP（可选）
if (window.RTCPeerConnection) {
  window.RTCPeerConnection = function() {
    return {
      addEventListener: function() {}
    };
  };
}

console.log('[hide.js] WebDriver 特征已隐藏');

