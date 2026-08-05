# Underwater Jam

Repository ini bakal dipakai buat development game kita selama Game Jam.

Simpan semua asset, script, dan progress project sesuai struktur folder yang udah ada supaya project tetap rapi yaa dan gampang dicari.

---

# Struktur Folder

## audio/

Semua file audio disimpan di sini.

- audio/bgm → Background music
- audio/sfx → Sound effect
- audio/voice → Voice (kalau nanti dipakai)

---

## images/

Semua asset gambar disimpan di sini.

- images/backgrounds → Background
- images/characters → Sprite karakter
- images/cg → CG / Illustration
- images/ui → Asset UI
- images/items → Item
- images/effects → Effect, particle, glow, vignette, dan sejenisnya

---

## story/

Semua script cerita.

Contoh:

- Prologue
- Chapter
- Side Quest
- Ending

---

## systems/

Semua gameplay system.

Contoh:

- Typing
- Inventory
- Affection
- Day & Night
- Map
- Save System

---

## screens/

Semua custom screen Ren'Py.

Contoh:

- Inventory Screen
- Map Screen
- Journal Screen
- Typing Screen

---

## characters/

Semua data character.

Contoh:

- MC
- NPC
- Fish
- Narrator

---

## Folder bawaan Ren'Py

Folder berikut merupakan folder bawaan Ren'Py.

- gui/
- libs/
- tl/
- cache/
- saves/

Kalau mau edit file bawaan Ren'Py, kabarin dulu supaya nggak bentrok sama yang lain.

---

# Branch

Repository ini menggunakan branch berikut.

## main

Berisi build yang sudah stabil atau versi final.

Jangan commit langsung ke branch ini.

---

## development

Semua fitur yang sudah selesai dikerjakan akan digabung ke branch ini.

Sebelum mulai kerja, selalu update branch ini dulu.

---

## feature/...

Setiap fitur dikerjakan di branch masing-masing.

Contoh:

- feature/story
- feature/ui
- feature/typing
- feature/audio
- feature/map
- feature/day-night

---

# Cara Mulai Ngerjain

1. Checkout ke branch `development`.

2. Pull dulu supaya project selalu versi terbaru.

3. Buat branch baru dari `development`.

Contoh:

```
feature/story
```

4. Kerjakan fitur.

5. Commit perubahan.

6. Push branch ke GitHub.

7. Buat Pull Request ke `development`.

Jangan commit langsung ke `main`.

---

# Penamaan File

Supaya nama file konsisten, gunakan format berikut.

Background

```
bg_school.png
bg_ocean.png
```

Character

```
char_mc_idle.png
char_fish_happy.png
```

CG

```
cg_good_ending.png
cg_intro.png
```

UI

```
ui_button_start.png
ui_inventory.png
```

Item

```
item_shell.png
item_pearl.png
```

BGM

```
bgm_title.ogg
bgm_underwater.ogg
```

SFX

```
sfx_click.wav
sfx_typing.wav
```

Story

```
prologue.rpy
chapter1.rpy
chapter2.rpy
ending.rpy
```

---

# Sebelum Commit

Sebelum commit, pastikan:

- Project masih bisa dijalankan.
- Tidak ada error.
- Nama file sudah sesuai.
- Hanya file yang memang dikerjakan yang ikut ke-commit.
- Tidak ada file cache, save, atau file `.rpyc` yang ikut ke-commit.

---

# Sebelum Push

Sebelum push, pastikan:

- Sudah pull dari `development`.
- Branch yang dipakai sudah benar.
- Commit sudah sesuai dengan perubahan yang dikerjakan.

---

# Pull Request

Sebelum membuat Pull Request:

- Pastikan project masih bisa dijalankan.
- Tidak ada error.
- Pull Request dibuat ke branch `development`, bukan `main`.
- Kalau ada merge conflict, selesaikan dulu sebelum merge.

---

# Commit Message

Gunakan commit message yang singkat dan jelas.

Contoh:

```
Add typing system
Fix dialogue bug
Update inventory UI
Add chapter 1
Change main menu
Fix typo
```

Hindari commit seperti:

```
fix
update
tes
123
wkwkwk
```

---

# Catatan

- Selalu pull `development` sebelum mulai kerja.
- Jangan commit langsung ke `main`.
- Jangan upload folder `cache`.
- Jangan upload folder `saves`.
- Jangan upload file `.rpyc`.
- Kalau mau edit file yang sama dengan orang lain, kabarin dulu supaya nggak merge conflict.
- Kalau bikin folder atau file baru yang dipakai semua orang, kabarin dulu di grup.
- Kalau bingung naruh asset atau script di mana, tanya dulu daripada nanti struktur project jadi berantakan.
- Sebelum merge, usahain cek lagi apakah semua perubahan memang sudah sesuai.

---

Semangat ngerjain game guys!!