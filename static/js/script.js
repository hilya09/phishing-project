// Toggle class active
const navbarNav = document.querySelector(".navbar-nav");
// Ketika humberger menu di klik
document.querySelector("#hamburger-menu").onclick = () => {
  navbarNav.classList.toggle("active");
};

// Klik di luar sidebar untuk menghilangkan nav
const hamburger = document.querySelector("#hamburger-menu");

document.addEventListener("click", function (e) {
  if (!hamburger.contains(e.target) && !navbarNav.contains(e.target)) {
    navbarNav.classList.remove("active");
  }
});

$(document).ready(function () {
  // -[Prediksi Model untuk Phishing Detection After Click Submit Button]---------------
  $("#prediksi_submit").click(function (e) {
    e.preventDefault();

    // Set data link url dari pengguna
    var input_link = $("#inputVal_link").val();
    // Panggil API dengan timeout 1 detik (1000 ms)
    setTimeout(function () {
      try {
        $.ajax({
          url: "/api/deteksi",
          type: "POST",
          data: { data: input_link },
          success: function (res) {
            // Ambil hasil prediksi link dari API
            var res_data_prediksi = res["data"];
            var note = res["note"];

            // Tampilkan hasil prediksi ke halaman web
            generate_prediksi(res_data_prediksi, note);
          },
        });
      } catch (e) {
        // Jika gagal memanggil API, tampilkan error di console
        console.log("Gagal !");
        console.log(e);
      }
    }, 1000);
  });

  // Fungsi untuk menampilkan hasil prediksi model
  function generate_prediksi(data_prediksi, note) {
    var str = "";
    str += "<p>Hasil Prediksi: </p>";
    str += "<p class='hasil-prediksi " + data_prediksi + "'>" + data_prediksi + "</p>";
    $("#hasil_prediksi").html(str);
    str += "<p>" + note + "</p>";
    $("#hasil_prediksi").html(str);
  }
});
