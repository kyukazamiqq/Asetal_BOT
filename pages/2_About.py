import streamlit as st

st.title("Tentang Kami")
st.markdown("Halo! kami adalah mahasiswa program studi sains data ITERA program studi Sains Data. Kami membuat project ini untuk membantu orang yang mempunyai masalah kesehatan mental dan memenuhi asesmen tugas besar mata kuliah Algoritma Pemrograman. ")

def main():
    st.title("Our Team")

    team_members = [
        {"name": "Nawwaf Abdurrahman", "nim": "122450018"},
        {"name": "Izza Lutfia", "nim": "122450090"},
        {"name": "Eka Fidya Putri", "nim": "122450045"},
        {"name": "Vira Maharani", "nim": "122450129"},
        # Tambahkan anggota tim lainnya sesuai kebutuhan
    ]

    for member in team_members:
        st.write(f"## {member['name']}")
        st.write(f"**NIM:** {member['nim']}")
        st.write("---")

    

if __name__ == "__main__":
    main()