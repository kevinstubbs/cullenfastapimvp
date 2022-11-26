async function onImageLoad(reader, file) {
  if (!file) throw new Error("onImageLoad called without file passed in.");

  const formData = new FormData();
  formData.append("file", file, file.name);
  formData.append("project_folder", "uploaded-project_folder");

  // TODO: Use async/await pattern instead.
  fetch("http://127.0.0.1:8000/uploadfile/t", {
    method: "post",
    body: formData,
    mode: "no-cors",
  })
    .then((response) => {
      console.log(response);
    })
    .catch((error) => {
      console.error(error);
    });

  const response = await fetch(
    "https://cullerwhale-classifier.hf.space/run/predict",
    {
      method: "POST",
      body: JSON.stringify({ data: [reader.result] }),
      headers: { "Content-Type": "application/json" },
    }
  );

  const facehuggerResults = await response.json();
  console.log("json", { facehuggerResults });

  // storing data from API call
  const caption = facehuggerResults["data"][0]["confidences"][0]["label"];
  const confidence = (
    100 * facehuggerResults["data"][0]["confidences"][0]["confidence"]
  ).toPrecision(4);
  console.log({ caption, confidence });

  // displaying data from API call
  const div = document.createElement("div");
  div.innerHTML = `<br/><img class="image-to-upload" fileName="${file.name}" confidence="${confidence}" src="${reader.result}" width="300" caption="${caption}"> <p>${caption}</p> <p>${confidence}<p>`;
  document.body.append(div);
}

// read files uploaded
function loadImage(file) {
  const reader = new FileReader();
  // console.log(file);
  reader.addEventListener("load", () => onImageLoad(reader, file));
  reader.readAsDataURL(file);
  // console.log(file);
}

photos.addEventListener("input", () => {
  [...photos.files].forEach(loadImage);
});

const createReportButton = document.getElementById("create-report");

createReportButton.addEventListener("click", async function () {
  const imagesToUpload = document.querySelectorAll(".image-to-upload");

  if (!imagesToUpload.length) {
    alert("Upload an image before creating a report.");
    return;
  }

  const data = await fetch("http://127.0.0.1:8000/input_metadata/", {
    method: "POST",
    headers: {
      Accept: "application/json, text/plain, */*",
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      data: [...imagesToUpload].map((x) => ({
        folder_name: "images",
        file_name: x.getAttribute("fileName"),
        caption: x.getAttribute("caption"),
        confidence: x.getAttribute("confidence"),
      })),
    }),
  });

  const reportname = (await data.text()).replace(/"/g, "");

  // Abort if the server didn't send any data back.
  if (!reportname.length) return;

  window.open(`http://127.0.0.1:8000/${reportname}`, "_blank").focus();
});
