const nav = document.querySelector(".primary-navigation");
const mobileButton = document.getElementById("mobileButton");

mobileButton.addEventListener("click", () => {
  const visibility = nav.getAttribute("data-something");
  // if the nav is closed, open it. Use data-attributes for JS
  if (visibility === "false") {
    nav.setAttribute("data-something", "true");
    mobileButton.setAttribute("aria-expanded", true);
  } else {
    nav.setAttribute("data-something", "false");
    mobileButton.setAttribute("aria-expanded", false);
  }

  console.log(visibility);

  // if the nav is open, close it
});

const tabList = document.querySelector('[role="tablist"]');
const tabs = tabList.querySelectorAll('[role="tab"]');

tabList.addEventListener("keydown", changeTabFocus);

tabs.forEach((tab) => {
  tab.addEventListener("click", changeTabPanel);
});

let tabFocus = 0;
function changeTabFocus(e) {
  const keydownLeft = 37;
  const keydownRight = 39;

  if (e.keyCode === keydownLeft || e.keyCode === keydownRight) {
    tabs[tabFocus].setAttribute("tabindex", -1);
  }

  if (e.keyCode === keydownRight) {
    tabFocus++;
    if (tabFocus >= tabs.length) {
      tabFocus = 0;
    }
  }

  if (e.keyCode === keydownLeft) {
    tabFocus--;
    if (tabFocus < 0) {
      tabFocus = tabs.length - 1;
    }
  }

  tabs[tabFocus].setAttribute("tabindex", 0);
  tabs[tabFocus].focus();
}

function changeTabPanel(e) {
  const targetTab = e.target;
  const targetPanel = targetTab.getAttribute("aria-controls");

  console.log(targetTab);
  console.log(targetPanel);

  const tabContainer = targetTab.parentNode;
  const mainContainer = tabContainer.parentNode;

  tabContainer
    .querySelector('[aria-selected="true"]')
    .setAttribute("aria-selected", false);

  targetTab.setAttribute("aria-selected", true);

  // we use parentNode to take a backwards step from the child. In this case, we are starting from the tab-list div and backing up twice to get to the main

  mainContainer
    .querySelectorAll('[role="tabpanel"]')
    .forEach((panel) => panel.setAttribute("hidden", true));

  mainContainer.querySelector([`#${targetPanel}`]).removeAttribute("hidden");
}

function hideContent(parent, content) {
  parent
    .querySelectorAll(content)
    .forEach((item) => panel.setAttribute("hidden", true));
}

// const jp_toggle = document.getElementById("jp");
// const eng_toggle = document.getElementById("eng");
// const eng_text = document.getElementById("eng-text");
// const jp_text = document.getElementById("jp-text");

// jp_toggle.addEventListener("click", () => {
//   eng_text.classList.add("hidden");
//   jp_text.classList.remove("hidden");
// });
// eng_toggle.addEventListener("click", () => {
//   jp_text.classList.add("hidden");
//   eng_text.classList.remove("hidden");
// });
