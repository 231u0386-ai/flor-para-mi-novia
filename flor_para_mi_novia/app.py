import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Una flor para ti ❤️",
    page_icon="🌷",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #160016, #3b003b, #130013);
}

h1, h2, h3, p {
    text-align: center;
    color: white !important;
}

div.stButton > button {
    display: block;
    margin: auto;
    background: #ff4b91;
    color: white;
    border-radius: 30px;
    padding: 12px 30px;
    font-size: 20px;
}
</style>
""", unsafe_allow_html=True)

st.title("Tengo algo para ti... ❤️")

st.markdown("""
<p style="font-size:20px;">
No podía darte esta flor en persona,<br>
así que decidí hacerte una que nunca se marchite. 🌷
</p>
""", unsafe_allow_html=True)

if st.button("🌷 Ver mi sorpresa"):

    mensaje = st.empty()
    dibujo = st.empty()

    mensaje.markdown(
        "<h3>Está floreciendo para ti... 🌱</h3>",
        unsafe_allow_html=True
    )

    # Crecimiento del tallo
    for progreso in np.linspace(0.1, 1, 20):

        fig, ax = plt.subplots(figsize=(6, 7))
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        y = np.linspace(-4, -4 + 4 * progreso, 100)
        x = 0.15 * np.sin(y * 1.5)

        ax.plot(x, y, linewidth=6, color="#2ecc71")

        ax.set_xlim(-4, 4)
        ax.set_ylim(-4.5, 4)
        ax.axis("off")

        dibujo.pyplot(fig)
        plt.close(fig)

        time.sleep(0.05)

    # Apertura de la flor
    for apertura in np.linspace(0.2, 1, 25):

        fig, ax = plt.subplots(figsize=(6, 7))
        fig.patch.set_alpha(0)
        ax.set_facecolor("none")

        # Tallo
        y = np.linspace(-4, 0, 100)
        x = 0.15 * np.sin(y * 1.5)

        ax.plot(x, y, linewidth=6, color="#2ecc71")

        # Pétalos
        for i in range(12):

            angulo = 2 * np.pi * i / 12
            distancia = 1.1 * apertura

            cx = distancia * np.cos(angulo)
            cy = distancia * np.sin(angulo)

            theta = np.linspace(0, 2 * np.pi, 100)

            px = (1.15 * apertura / 2) * np.cos(theta)
            py = (2 * apertura / 2) * np.sin(theta)

            xr = (
                px * np.cos(angulo)
                - py * np.sin(angulo)
                + cx
            )

            yr = (
                px * np.sin(angulo)
                + py * np.cos(angulo)
                + cy
            )

            ax.fill(xr, yr, color="#ff4f9a", alpha=0.85)

        # Centro amarillo
        centro = plt.Circle(
            (0, 0),
            0.65 * apertura,
            color="#ffd166"
        )

        ax.add_patch(centro)

        ax.set_xlim(-4, 4)
        ax.set_ylim(-4.5, 4)
        ax.axis("off")

        dibujo.pyplot(fig)
        plt.close(fig)

        time.sleep(0.05)

    mensaje.empty()

    st.markdown("""
    <div style="
        text-align:center;
        padding:25px;
        background:rgba(255,255,255,0.08);
        border-radius:25px;
    ">

    <h1 style="color:#ff77aa !important;">
    Para ti, mi amor ❤️
    </h1>

    <p style="font-size:21px; line-height:1.7;">

    Tal vez esta flor está hecha con código,<br>
    pero cada línea la hice pensando en ti. 🌷

    <br><br>

    Gracias por hacer mis días más bonitos,
    por cada momento, cada sonrisa
    y cada recuerdo que hemos creado juntas.

    <br><br>

    Si pudiera regalarte una flor
    por cada vez que pienso en ti,
    tendría un jardín infinito. 💕

    </p>

    <h2 style="color:#ffb3d1 !important;">
    Te amo ❤️
    </h2>

    </div>
    """, unsafe_allow_html=True)

    st.balloons()