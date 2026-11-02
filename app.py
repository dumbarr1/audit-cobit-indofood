"""
app.py - Aplikasi Web Audit Sistem Informasi PT Indofood (COBIT 5)
Mata kuliah : Audit Sistem Informasi - Tugas 2
Teknologi   : Python + Streamlit + pandas

Cara menjalankan (di terminal / CMD, di dalam folder file ini):
    pip install -r requirements.txt
    streamlit run app.py
"""

# =====================================================================
# BAGIAN 1 - DATA KERANGKA KERJA COBIT 5 (5 DOMAIN, 37 PROSES)
# Data ini sama dengan form audit Word yang sudah Anda buat.
# =====================================================================
DOMAIN_COBIT = [
    {"kode": "EDM", "nama": "Evaluate, Direct and Monitor",
     "deskripsi": "Tata kelola TI: dewan direksi mengevaluasi, mengarahkan, dan memantau pemanfaatan TI.",
     "proses": [
        ("EDM01", "Ensure Governance Framework Setting and Maintenance", "Apakah kerangka tata kelola TI telah ditetapkan, disetujui Direksi, dan ditinjau secara berkala?", "Piagam/kebijakan tata kelola TI, notulen rapat Direksi atau Komite TI, struktur organisasi"),
        ("EDM02", "Ensure Benefits Delivery", "Apakah investasi TI (mis. ERP, sistem distribusi, sistem pabrik) dievaluasi manfaatnya terhadap tujuan bisnis?", "Business case, laporan realisasi manfaat, KPI TI"),
        ("EDM03", "Ensure Risk Optimisation", "Apakah selera risiko (risk appetite) TI ditetapkan dan terintegrasi dengan manajemen risiko perusahaan?", "Kebijakan manajemen risiko, risk register, laporan profil risiko"),
        ("EDM04", "Ensure Resource Optimisation", "Apakah SDM, anggaran, dan infrastruktur TI dialokasikan secara optimal sesuai prioritas bisnis?", "Anggaran TI, rencana kapasitas, rencana SDM TI"),
        ("EDM05", "Ensure Stakeholder Transparency", "Apakah kinerja dan kepatuhan TI dilaporkan secara transparan kepada pemangku kepentingan?", "Laporan kinerja TI, laporan tahunan, laporan kepatuhan"),
     ]},
    {"kode": "APO", "nama": "Align, Plan and Organise",
     "deskripsi": "Perencanaan dan pengorganisasian TI agar selaras dengan strategi bisnis.",
     "proses": [
        ("APO01", "Manage the IT Management Framework", "Apakah kebijakan, standar, dan SOP TI telah terdokumentasi, disahkan, dan dikomunikasikan?", "Dokumen kebijakan & SOP TI, bukti sosialisasi, daftar distribusi dokumen"),
        ("APO02", "Manage Strategy", "Apakah rencana strategis TI selaras dengan strategi bisnis grup dan ditinjau berkala?", "Renstra/roadmap TI, strategi bisnis, notulen reviu"),
        ("APO03", "Manage Enterprise Architecture", "Apakah arsitektur enterprise (bisnis, data, aplikasi, infrastruktur) terdokumentasi dan dipelihara?", "Diagram arsitektur, inventaris aplikasi, kamus data"),
        ("APO04", "Manage Innovation", "Apakah terdapat proses evaluasi teknologi baru untuk meningkatkan nilai bisnis?", "Kajian teknologi, proposal inovasi, hasil uji coba (pilot)"),
        ("APO05", "Manage Portfolio", "Apakah program dan proyek TI diprioritaskan melalui mekanisme portofolio yang jelas?", "Daftar portofolio proyek, kriteria prioritas, persetujuan investasi"),
        ("APO06", "Manage Budget and Costs", "Apakah anggaran TI disusun, dipantau realisasinya, dan deviasi dianalisis?", "RKAP TI, laporan realisasi anggaran, analisis varians"),
        ("APO07", "Manage Human Resources", "Apakah kompetensi, pelatihan, dan rencana suksesi/backup personel kunci TI dikelola?", "Matriks kompetensi, rencana pelatihan, data turnover"),
        ("APO08", "Manage Relationships", "Apakah hubungan TI dengan unit bisnis dikelola secara terstruktur?", "Notulen pertemuan, survei kepuasan, daftar PIC bisnis"),
        ("APO09", "Manage Service Agreements", "Apakah layanan TI memiliki SLA/OLA yang terdefinisi dan dipantau pencapaiannya?", "Katalog layanan, dokumen SLA/OLA, laporan pencapaian SLA"),
        ("APO10", "Manage Suppliers", "Apakah vendor/penyedia TI (termasuk cloud dan outsourcing) diseleksi, dikontrol, dan dievaluasi kinerjanya?", "Kontrak vendor, evaluasi vendor, perjanjian kerahasiaan"),
        ("APO11", "Manage Quality", "Apakah standar dan sistem manajemen mutu TI diterapkan dan diukur?", "Standar mutu, hasil reviu kualitas, laporan perbaikan"),
        ("APO12", "Manage Risk", "Apakah risiko TI diidentifikasi, dianalisis, dan ditindaklanjuti dengan rencana mitigasi?", "Risk register TI, hasil asesmen risiko, rencana mitigasi"),
        ("APO13", "Manage Security", "Apakah sistem manajemen keamanan informasi (ISMS) ditetapkan, diterapkan, dan dievaluasi?", "Kebijakan keamanan informasi, sertifikasi/asesmen ISMS, laporan audit keamanan"),
     ]},
    {"kode": "BAI", "nama": "Build, Acquire and Implement",
     "deskripsi": "Pengadaan, pengembangan, dan implementasi solusi TI serta pengelolaan perubahan.",
     "proses": [
        ("BAI01", "Manage Programmes and Projects", "Apakah proyek TI dikelola dengan metodologi baku (rencana, jadwal, risiko, pelaporan)?", "Project charter, rencana proyek, laporan progres, lessons learned"),
        ("BAI02", "Manage Requirements Definition", "Apakah kebutuhan bisnis dan sistem didefinisikan, divalidasi, dan disetujui pengguna?", "Dokumen kebutuhan (BRD/SRS), matriks keterlacakan, persetujuan pengguna"),
        ("BAI03", "Manage Solutions Identification and Build", "Apakah pengembangan/pengadaan solusi mengikuti standar dan melalui pengujian yang memadai?", "Desain solusi, skenario & hasil uji (UAT), standar pengembangan aman"),
        ("BAI04", "Manage Availability and Capacity", "Apakah ketersediaan dan kapasitas sistem kritis dipantau dan diproyeksikan?", "Laporan kapasitas, monitoring uptime, rencana peningkatan kapasitas"),
        ("BAI05", "Manage Organisational Change Enablement", "Apakah dampak perubahan sistem terhadap organisasi dikelola (komunikasi, pelatihan pengguna)?", "Rencana komunikasi perubahan, materi pelatihan, daftar hadir"),
        ("BAI06", "Manage Changes", "Apakah perubahan sistem diajukan, dinilai, disetujui, diuji, dan didokumentasikan (change management)?", "Formulir permintaan perubahan, log perubahan, persetujuan CAB"),
        ("BAI07", "Manage Change Acceptance and Transitioning", "Apakah serah terima ke produksi didahului UAT, rencana rollback, dan persetujuan formal?", "Berita acara UAT, rencana migrasi/rollback, sign-off go-live"),
        ("BAI08", "Manage Knowledge", "Apakah pengetahuan sistem (manual, dokumentasi teknis) tersedia dan dimutakhirkan?", "Repositori pengetahuan, manual pengguna, dokumentasi teknis"),
        ("BAI09", "Manage Assets", "Apakah aset TI (perangkat keras, perangkat lunak, lisensi) diinventarisasi dan dikelola siklus hidupnya?", "Daftar aset TI, register lisensi, laporan stock opname aset"),
        ("BAI10", "Manage Configuration", "Apakah konfigurasi sistem dan item konfigurasi (CMDB) dicatat dan dikendalikan?", "CMDB, baseline konfigurasi, laporan audit konfigurasi"),
     ]},
    {"kode": "DSS", "nama": "Deliver, Service and Support",
     "deskripsi": "Penyampaian layanan operasional TI, dukungan pengguna, kontinuitas, dan keamanan.",
     "proses": [
        ("DSS01", "Manage Operations", "Apakah operasional TI (job scheduling, backup, pemantauan, pusat data) berjalan sesuai prosedur?", "SOP operasional, log job & backup, laporan monitoring, kontrol akses fisik data center"),
        ("DSS02", "Manage Service Requests and Incidents", "Apakah permintaan layanan dan insiden dicatat, diprioritaskan, diselesaikan, dan dilaporkan?", "Log service desk, laporan insiden, metrik waktu penyelesaian"),
        ("DSS03", "Manage Problems", "Apakah akar penyebab insiden berulang dianalisis dan ditindaklanjuti?", "Register masalah, laporan root cause analysis, tindakan korektif"),
        ("DSS04", "Manage Continuity", "Apakah BCP/DRP tersedia, diuji, dan dimutakhirkan untuk sistem kritis?", "Dokumen BCP/DRP, hasil uji DR, RTO/RPO, bukti pemulihan backup"),
        ("DSS05", "Manage Security Services", "Apakah kontrol keamanan (akses logis, antivirus, patching, firewall, hak akses) efektif?", "Daftar user & hak akses, log akses, hasil vulnerability scan/pentest, laporan patching"),
        ("DSS06", "Manage Business Process Controls", "Apakah kontrol aplikasi (input, proses, output, segregation of duties) pada proses bisnis kritis memadai?", "Matriks SoD, laporan exception, hasil pengujian kontrol aplikasi"),
     ]},
    {"kode": "MEA", "nama": "Monitor, Evaluate and Assess",
     "deskripsi": "Pemantauan kinerja, evaluasi pengendalian internal, dan kepatuhan terhadap regulasi.",
     "proses": [
        ("MEA01", "Monitor, Evaluate and Assess Performance and Conformance", "Apakah kinerja TI diukur dengan indikator yang jelas dan hasilnya ditindaklanjuti?", "Dashboard KPI/KRI TI, laporan kinerja bulanan, tindak lanjut hasil"),
        ("MEA02", "Monitor, Evaluate and Assess the System of Internal Control", "Apakah efektivitas pengendalian internal TI dievaluasi dan kelemahan diperbaiki?", "Laporan audit internal/eksternal, self-assessment kontrol, status tindak lanjut temuan"),
        ("MEA03", "Monitor, Evaluate and Assess Compliance with External Requirements", "Apakah kepatuhan terhadap regulasi (UU PDP, UU ITE, ketentuan OJK/BEI) dipantau?", "Daftar regulasi, matriks kepatuhan, laporan kepatuhan, bukti perlindungan data pribadi"),
     ]},
]

# Pilihan penilaian
OPSI_HASIL = ["Belum dinilai", "Ya", "Sebagian", "Tidak"]
SKOR_HASIL = {"Ya": 1.0, "Sebagian": 0.5, "Tidak": 0.0}   # untuk persentase kepatuhan
NAMA_LEVEL = {
    0: "0 - Incomplete", 1: "1 - Performed", 2: "2 - Managed",
    3: "3 - Established", 4: "4 - Predictable", 5: "5 - Optimising",
}
TARGET_DEFAULT = 3   # target umum: proses 'Established' (terdefinisi baku)

# Teks otomatis untuk temuan (silakan diubah sesuai kebutuhan tugas)
DAMPAK_DOMAIN = {
    "EDM": "Arah dan pengawasan TI oleh pimpinan lemah sehingga investasi dan risiko TI kurang terkendali.",
    "APO": "Perencanaan dan pengorganisasian TI tidak selaras dengan bisnis sehingga sumber daya terpakai tidak efektif.",
    "BAI": "Solusi atau perubahan sistem berisiko gagal, tidak sesuai kebutuhan, atau menimbulkan gangguan operasional.",
    "DSS": "Layanan operasional terganggu dan keamanan/kontinuitas sistem kritis berisiko tidak terjaga.",
    "MEA": "Kinerja, pengendalian, dan kepatuhan TI tidak terpantau sehingga penyimpangan terlambat terdeteksi.",
}
REKOMENDASI_DOMAIN = {
    "EDM": "Tetapkan/perbarui kebijakan dan mekanisme evaluasi serta pelaporan tata kelola TI kepada Direksi.",
    "APO": "Dokumentasikan dan sosialisasikan kebijakan, rencana, dan prosedur pengelolaan TI yang selaras strategi bisnis.",
    "BAI": "Terapkan prosedur baku pengelolaan proyek, perubahan, dan serah terima sistem lengkap dengan bukti persetujuan.",
    "DSS": "Perkuat prosedur operasional, penanganan insiden, kontinuitas, dan kontrol keamanan serta lakukan pengujian berkala.",
    "MEA": "Tetapkan indikator kinerja dan jadwal evaluasi kontrol serta matriks kepatuhan regulasi yang ditinjau berkala.",
}


# =====================================================================
# BAGIAN 2 - LOGIKA PERHITUNGAN (tidak tergantung tampilan)
# Fungsi-fungsi ini dipakai oleh versi Colab maupun Streamlit.
# =====================================================================
import io
import json
from datetime import datetime

import pandas as pd


def daftar_proses():
    """Mengubah struktur DOMAIN_COBIT menjadi daftar datar (flat list)."""
    hasil = []
    for d in DOMAIN_COBIT:
        for kode, nama, tanya, bukti in d["proses"]:
            hasil.append({"domain": d["kode"], "kode": kode, "proses": nama,
                          "pertanyaan": tanya, "bukti": bukti})
    return hasil


def jawaban_kosong():
    """Membuat jawaban awal: semua proses 'Belum dinilai'."""
    return {p["kode"]: {"hasil": "Belum dinilai", "level": 0,
                        "target": TARGET_DEFAULT, "catatan": ""}
            for p in daftar_proses()}


def buat_df_penilaian(jawaban):
    """Menggabungkan data proses dengan jawaban auditor menjadi satu tabel."""
    baris = []
    for p in daftar_proses():
        j = jawaban.get(p["kode"], {"hasil": "Belum dinilai", "level": 0,
                                    "target": TARGET_DEFAULT, "catatan": ""})
        gap = max(int(j["target"]) - int(j["level"]), 0)
        baris.append({
            "Domain": p["domain"], "Kode": p["kode"], "Proses": p["proses"],
            "Pertanyaan Audit": p["pertanyaan"], "Hasil": j["hasil"],
            "Level Aktual": int(j["level"]), "Level Target": int(j["target"]),
            "Gap": gap, "Catatan": j["catatan"],
        })
    return pd.DataFrame(baris)


def buat_rekap_domain(df):
    """Rekap per domain. Hanya proses yang SUDAH dinilai yang dihitung."""
    baris = []
    for d in DOMAIN_COBIT:
        sub = df[df["Domain"] == d["kode"]]
        dinilai = sub[sub["Hasil"] != "Belum dinilai"]
        n = len(dinilai)
        if n:
            skor = dinilai["Hasil"].map(SKOR_HASIL).mean() * 100
            aktual, target = dinilai["Level Aktual"].mean(), dinilai["Level Target"].mean()
        else:
            skor = aktual = target = 0.0
        baris.append({
            "Domain": d["kode"], "Nama Domain": d["nama"],
            "Jumlah Proses": len(sub), "Sudah Dinilai": n,
            "Level Aktual": round(aktual, 2), "Level Target": round(target, 2),
            "Gap": round(max(target - aktual, 0), 2),
            "Kepatuhan (%)": round(skor, 1),
        })
    return pd.DataFrame(baris)


def ringkasan_total(df):
    """Angka ringkasan untuk seluruh audit."""
    dinilai = df[df["Hasil"] != "Belum dinilai"]
    n = len(dinilai)
    return {
        "total_proses": len(df), "dinilai": n,
        "progres_pct": round(n / len(df) * 100, 1) if len(df) else 0,
        "rata_level": round(dinilai["Level Aktual"].mean(), 2) if n else 0.0,
        "kepatuhan_pct": round(dinilai["Hasil"].map(SKOR_HASIL).mean() * 100, 1) if n else 0.0,
    }


def tingkat_risiko(hasil, gap):
    """Aturan sederhana penentuan tingkat risiko temuan (boleh Anda ubah)."""
    if hasil == "Tidak" or gap >= 2:
        return "Tinggi"
    if hasil == "Sebagian" or gap == 1:
        return "Sedang"
    return "Rendah"


def buat_temuan(df):
    """Membuat draft temuan otomatis untuk proses yang bermasalah."""
    baris = []
    dinilai = df[df["Hasil"] != "Belum dinilai"]
    for _, r in dinilai.iterrows():
        if r["Hasil"] == "Ya" and r["Gap"] == 0:
            continue   # tidak ada masalah -> tidak jadi temuan
        deskripsi = (f"Aktivitas '{r['Pertanyaan Audit']}' dinilai {r['Hasil']}. "
                     f"Level kapabilitas aktual {r['Level Aktual']} dari target {r['Level Target']}.")
        if str(r["Catatan"]).strip():
            deskripsi += f" Catatan auditor: {r['Catatan']}"
        baris.append({
            "No": len(baris) + 1, "Ref. Proses": r["Kode"],
            "Deskripsi Temuan": deskripsi,
            "Kriteria": f"COBIT 5 - {r['Kode']} {r['Proses']}",
            "Dampak / Risiko": DAMPAK_DOMAIN[r["Domain"]],
            "Rekomendasi": REKOMENDASI_DOMAIN[r["Domain"]],
            "Tingkat Risiko": tingkat_risiko(r["Hasil"], r["Gap"]),
        })
    kolom = ["No", "Ref. Proses", "Deskripsi Temuan", "Kriteria",
             "Dampak / Risiko", "Rekomendasi", "Tingkat Risiko"]
    return pd.DataFrame(baris, columns=kolom)


def cek_konsistensi(df):
    """Mencari penilaian yang janggal supaya auditor memeriksa ulang."""
    pesan = []
    for _, r in df[df["Hasil"] != "Belum dinilai"].iterrows():
        if r["Hasil"] == "Ya" and r["Level Aktual"] <= 1:
            pesan.append(f"{r['Kode']}: hasil 'Ya' tetapi level hanya {r['Level Aktual']}. Periksa lagi.")
        if r["Hasil"] == "Tidak" and r["Level Aktual"] >= 3:
            pesan.append(f"{r['Kode']}: hasil 'Tidak' tetapi level {r['Level Aktual']}. Periksa lagi.")
    return pesan


def ekspor_excel(info, df, rekap, temuan):
    """Membuat file Excel (dalam memori) berisi 4 sheet. Mengembalikan bytes."""
    buf = io.BytesIO()
    info_df = pd.DataFrame(list(info.items()), columns=["Keterangan", "Isi"])
    with pd.ExcelWriter(buf, engine="openpyxl") as xw:
        info_df.to_excel(xw, sheet_name="Info Audit", index=False)
        df.to_excel(xw, sheet_name="Penilaian", index=False)
        rekap.to_excel(xw, sheet_name="Rekap Domain", index=False)
        temuan.to_excel(xw, sheet_name="Temuan", index=False)
        for ws in xw.book.worksheets:          # lebar kolom otomatis
            for kolom in ws.columns:
                panjang = max(len(str(c.value)) if c.value is not None else 0 for c in kolom)
                ws.column_dimensions[kolom[0].column_letter].width = min(panjang + 2, 60)
            ws.freeze_panes = "A2"
    return buf.getvalue()


def ekspor_json(info, jawaban):
    """Menyimpan progres audit ke teks JSON agar bisa dilanjutkan nanti."""
    return json.dumps({"info": info, "jawaban": jawaban}, ensure_ascii=False, indent=2)


def impor_json(teks):
    """Membaca progres yang tersimpan. Mengembalikan (info, jawaban)."""
    data = json.loads(teks)
    jawaban = jawaban_kosong()
    for kode, nilai in data.get("jawaban", {}).items():
        if kode in jawaban:
            jawaban[kode].update(nilai)
    return data.get("info", {}), jawaban


def waktu_sekarang():
    return datetime.now().strftime("%Y%m%d_%H%M")


def contoh_jawaban(seed=42):
    """DATA CONTOH (dummy) untuk mencoba aplikasi. Bukan hasil audit sungguhan!"""
    import random
    acak = random.Random(seed)
    jawaban = jawaban_kosong()
    for kode in jawaban:
        hasil = acak.choices(["Ya", "Sebagian", "Tidak"], weights=[45, 40, 15])[0]
        level = {"Ya": acak.choice([3, 4]), "Sebagian": acak.choice([2, 2, 3]),
                 "Tidak": acak.choice([0, 1])}[hasil]
        jawaban[kode] = {"hasil": hasil, "level": level, "target": TARGET_DEFAULT,
                         "catatan": "Data contoh (dummy) - ganti dengan temuan sebenarnya."}
    return jawaban


# =====================================================================
# BAGIAN 3 - TAMPILAN WEB (STREAMLIT)
# =====================================================================
import streamlit as st

st.set_page_config(page_title="Audit SI COBIT 5 - PT Indofood", page_icon="🛡️", layout="wide")

KUNCI_INFO = {"Auditor": "info_auditor", "Auditee": "info_auditee", "Unit/Divisi": "info_unit",
              "Periode Audit": "info_periode", "Lokasi": "info_lokasi"}


# ---- Inisialisasi 'ingatan' aplikasi (session_state) ----
def terapkan_ke_state(jawaban, info=None):
    for kode, nilai in jawaban.items():
        for nama, isi in nilai.items():
            st.session_state[f"{nama}_{kode}"] = isi
    for label, kunci in KUNCI_INFO.items():
        if info and label in info:
            st.session_state[kunci] = info[label]


if "siap" not in st.session_state:
    terapkan_ke_state(jawaban_kosong())
    for kunci in KUNCI_INFO.values():
        st.session_state[kunci] = ""
    st.session_state["siap"] = True


def ambil_jawaban():
    return {p["kode"]: {n: st.session_state[f"{n}_{p['kode']}"]
                        for n in ("hasil", "level", "target", "catatan")}
            for p in daftar_proses()}


def ambil_info():
    info = {"Nama Perusahaan": "PT Indofood Sukses Makmur Tbk", "Kerangka Kerja": "COBIT 5"}
    info.update({label: st.session_state[kunci] for label, kunci in KUNCI_INFO.items()})
    return info


def cb_contoh():
    terapkan_ke_state(contoh_jawaban())


def cb_reset():
    terapkan_ke_state(jawaban_kosong())


# ---- Sidebar ----
with st.sidebar:
    st.header("Informasi Audit")
    st.text("PT Indofood Sukses Makmur Tbk")
    st.text("Kerangka kerja: COBIT 5")

    # Muat progres dari file JSON (harus sebelum widget lain dibuat)
    berkas = st.file_uploader("Muat progres (.json)", type="json")
    if berkas is not None:
        penanda = f"{berkas.name}-{berkas.size}"
        if st.session_state.get("_berkas_dimuat") != penanda:
            info_muat, jawaban_muat = impor_json(berkas.getvalue().decode("utf-8"))
            terapkan_ke_state(jawaban_muat, info_muat)
            st.session_state["_berkas_dimuat"] = penanda
            st.rerun()

    for label, kunci in KUNCI_INFO.items():
        st.text_input(label, key=kunci)

    df_side = buat_df_penilaian(ambil_jawaban())
    rg = ringkasan_total(df_side)
    st.progress(rg["progres_pct"] / 100, text=f"Progres: {rg['dinilai']}/{rg['total_proses']} proses")
    st.button("Isi data contoh (dummy)", on_click=cb_contoh)
    st.button("Reset semua penilaian", on_click=cb_reset)

# ---- Halaman utama ----
st.title("Aplikasi Audit Sistem Informasi - PT Indofood")
st.caption("Berbasis COBIT 5 (EDM, APO, BAI, DSS, MEA). Isi tab Penilaian, lalu lihat Dashboard, Temuan, dan Export.")

tab_nilai, tab_dash, tab_temuan, tab_export = st.tabs(["Penilaian", "Dashboard", "Temuan", "Export"])

# ---- TAB 1: PENILAIAN ----
with tab_nilai:
    with st.expander("Panduan skala level kapabilitas (klik untuk membuka)"):
        st.markdown("""
| Level | Nama | Arti singkat |
|---|---|---|
| 0 | Incomplete | Proses tidak ada / gagal mencapai tujuan |
| 1 | Performed | Proses berjalan tetapi belum terkelola formal |
| 2 | Managed | Proses terencana, dipantau, dan terdokumentasi |
| 3 | Established | Proses mengikuti standar baku di seluruh organisasi |
| 4 | Predictable | Proses terukur dan dikendalikan secara kuantitatif |
| 5 | Optimising | Proses terus diperbaiki secara berkelanjutan |
""")
    sub_tab = st.tabs([f"{d['kode']}" for d in DOMAIN_COBIT])
    for tab_d, d in zip(sub_tab, DOMAIN_COBIT):
        with tab_d:
            st.subheader(f"{d['kode']} - {d['nama']}")
            st.caption(d["deskripsi"])
            for kode, nama, tanya, bukti in d["proses"]:
                status = st.session_state[f"hasil_{kode}"]
                with st.expander(f"{kode} - {nama}   [{status}]"):
                    st.write(f"**Pertanyaan audit:** {tanya}")
                    st.write(f"**Bukti yang diperiksa:** {bukti}")
                    st.radio("Hasil penilaian", OPSI_HASIL, horizontal=True, key=f"hasil_{kode}")
                    k1, k2 = st.columns(2)
                    k1.slider("Level aktual (0-5)", 0, 5, key=f"level_{kode}")
                    k2.slider("Level target (0-5)", 0, 5, key=f"target_{kode}")
                    st.text_area("Catatan / temuan auditor", key=f"catatan_{kode}")

# ---- Hitung semua hasil (dipakai tab berikutnya) ----
df = buat_df_penilaian(ambil_jawaban())
rekap = buat_rekap_domain(df)
temuan = buat_temuan(df)
rg = ringkasan_total(df)

# ---- TAB 2: DASHBOARD ----
with tab_dash:
    if rg["dinilai"] == 0:
        st.info("Belum ada proses yang dinilai. Isi dulu di tab Penilaian, atau klik 'Isi data contoh' di sidebar.")
    else:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Proses dinilai", f"{rg['dinilai']}/{rg['total_proses']}")
        m2.metric("Rata-rata level", rg["rata_level"], NAMA_LEVEL[round(rg["rata_level"])], delta_color="off")
        m3.metric("Kepatuhan", f"{rg['kepatuhan_pct']}%")
        m4.metric("Jumlah temuan", len(temuan))

        st.subheader("Level kapabilitas aktual vs target per domain")
        st.bar_chart(rekap.set_index("Domain")[["Level Aktual", "Level Target"]])
        st.subheader("Rekap per domain")
        st.dataframe(rekap)

        pesan = cek_konsistensi(df)
        if pesan:
            st.warning("Ada penilaian yang perlu dicek ulang:\n\n" + "\n".join(f"- {x}" for x in pesan))
        st.subheader("Seluruh hasil penilaian")
        st.dataframe(df)

# ---- TAB 3: TEMUAN ----
with tab_temuan:
    if len(temuan) == 0:
        st.info("Belum ada temuan. Temuan dibuat otomatis dari proses yang dinilai 'Sebagian'/'Tidak' atau yang levelnya di bawah target.")
    else:
        st.caption("Ini DRAFT otomatis. Sebagai auditor, Anda wajib memeriksa dan menyempurnakan isinya.")
        hitung = temuan["Tingkat Risiko"].value_counts()
        c1, c2, c3 = st.columns(3)
        c1.metric("Risiko Tinggi", int(hitung.get("Tinggi", 0)))
        c2.metric("Risiko Sedang", int(hitung.get("Sedang", 0)))
        c3.metric("Risiko Rendah", int(hitung.get("Rendah", 0)))
        st.dataframe(temuan)

# ---- TAB 4: EXPORT ----
with tab_export:
    st.write("Unduh hasil audit untuk dilampirkan pada laporan tugas Anda.")
    stempel = waktu_sekarang()
    st.download_button("Unduh Excel (Info, Penilaian, Rekap, Temuan)",
                       data=ekspor_excel(ambil_info(), df, rekap, temuan),
                       file_name=f"Hasil_Audit_COBIT5_{stempel}.xlsx",
                       mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    st.download_button("Unduh CSV Penilaian", data=df.to_csv(index=False).encode("utf-8"),
                       file_name=f"Penilaian_{stempel}.csv", mime="text/csv")
    st.download_button("Simpan progres (JSON)", data=ekspor_json(ambil_info(), ambil_jawaban()),
                       file_name=f"Progres_Audit_{stempel}.json", mime="application/json")
