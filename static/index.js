const submitBtn = document.querySelector("#submit");
const urlInput = document.querySelector("#url-input");
const shortUrlEl = document.querySelector("#short-url");
const shortUrlTextEl = document.querySelector("#short-url-text");
const copyBtn = document.querySelector("#copy-btn");
const copyFeedbackEl = document.querySelector("#copy-feedback");
const inputErrorEl = document.querySelector("#input-error");

urlInput.focus();

const urlRegex =
  /https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)/i;

function isValidUrl(url) {
  return urlRegex.test(url);
}

function elVisible(el) {
  el.classList.remove("d-none");
}

function elHide(el) {
  el.classList.add("d-none");
}

function setInvalidUrl() {
  urlInput.classList.add("input-error");
  elVisible(inputErrorEl);
}

function setValidUrl() {
  urlInput.classList.remove("input-error");
  elHide(inputErrorEl);
}

function submitURL(e) {
  if (e) {
    e.preventDefault();
  }

  const url = urlInput.value;

  if (!isValidUrl(url)) {
    setInvalidUrl();
    return;
  }

  setValidUrl();

  fetch("/url", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      url,
    }),
  })
    .then((resp) => resp.json())
    .then(({ short_url }) => {
      elVisible(shortUrlEl);
      shortUrlTextEl.innerText = short_url;
    })
    .catch((err) => console.error({ err }));
}

submitBtn.onclick = submitURL;
submitBtn.addEventListener("keydown", ({ key }) => {
  if (key === "Enter") {
    submitURL();
  }
});

copyBtn.onclick = () => {
  navigator.clipboard.writeText(shortUrlTextEl.innerText);
  elVisible(copyFeedbackEl);
};
