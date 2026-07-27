import streamlit as st
import numpy as np
import cv2
from PIL import Image
import io

st.set_page_config(
    page_title="Traffic Density Detection",
    page_icon="🚦",
    layout="wide",
)

# ── Styling ──────────────────────────────────────────────────────────
st.markdown("""
<style>
.big-title{font-size:2rem;font-weight:800;margin-bottom:0;}
.subtitle{color:#888;margin-top:0;margin-bottom:1.5rem;}
.result-box{background:#111827;border:1px solid #2c3444;border-radius:10px;
            padding:1.2rem;margin-top:1rem;}
.metric-label{color:#9ca3af;font-size:0.85rem;text-transform:uppercase;letter-spacing:.04em;}
.metric-value{font-size:1.8rem;font-weight:700;color:#5eead4;}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">🚦 Real-Time Traffic Density Detection</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">Computer vision system using Canny Edge Detection to estimate '
    'traffic density and dynamically allocate green-signal timing.</p>',
    unsafe_allow_html=True,
)

# ── Core detection logic ────────────────────────────────────────────

def to_gray(img_array: np.ndarray) -> np.ndarray:
    if img_array.ndim == 3:
        return cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
    return img_array

def auto_canny(image: np.ndarray, sigma: float = 0.33) -> np.ndarray:
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    return cv2.Canny(image, lower, upper)

def white_pixel_count(edge_img: np.ndarray) -> int:
    return int(np.sum(edge_img == 255))

def allocate_time(density_pct: float) -> tuple[str, int]:
    if density_pct >= 90:
        return "Very High", 60
    elif density_pct > 85:
        return "High", 50
    elif density_pct > 75:
        return "Moderate", 40
    elif density_pct > 50:
        return "Low", 30
    else:
        return "Very Low", 20

# ── UI: two-column upload ───────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("1️⃣ Reference Image (empty / baseline road)")
    ref_file = st.file_uploader("Upload reference image", type=["png", "jpg", "jpeg"], key="ref")

with col2:
    st.subheader("2️⃣ Sample Image (current traffic)")
    sample_file = st.file_uploader("Upload traffic image to analyze", type=["png", "jpg", "jpeg"], key="sample")

st.divider()

if ref_file and sample_file:
    ref_img = np.array(Image.open(ref_file).convert("RGB"))
    sample_img = np.array(Image.open(sample_file).convert("RGB"))

    ref_gray = to_gray(ref_img)
    sample_gray = to_gray(sample_img)

    ref_edges = auto_canny(ref_gray)
    sample_edges = auto_canny(sample_gray)

    ref_pixels = white_pixel_count(ref_edges)
    sample_pixels = white_pixel_count(sample_edges)

    density_pct = (sample_pixels / ref_pixels * 100) if ref_pixels > 0 else 0
    level, seconds = allocate_time(density_pct)

    st.subheader("🖼 Edge Detection Output")
    c1, c2, c3, c4 = st.columns(4)
    c1.image(ref_img, caption="Reference (original)", use_container_width=True)
    c2.image(ref_edges, caption="Reference (edges)", use_container_width=True)
    c3.image(sample_img, caption="Sample (original)", use_container_width=True)
    c4.image(sample_edges, caption="Sample (edges)", use_container_width=True)

    st.markdown('<div class="result-box">', unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1:
        st.markdown('<p class="metric-label">Reference White Pixels</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="metric-value">{ref_pixels:,}</p>', unsafe_allow_html=True)
    with m2:
        st.markdown('<p class="metric-label">Sample White Pixels</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="metric-value">{sample_pixels:,}</p>', unsafe_allow_html=True)
    with m3:
        st.markdown('<p class="metric-label">Traffic Density</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="metric-value">{density_pct:.1f}%</p>', unsafe_allow_html=True)
    with m4:
        st.markdown('<p class="metric-label">Green Signal Time</p>', unsafe_allow_html=True)
        st.markdown(f'<p class="metric-value">{seconds}s</p>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    st.success(f"**Traffic level: {level}** — allocate **{seconds} seconds** of green signal time.")

else:
    st.info("👆 Upload both a reference image and a sample traffic image to run the analysis.")
    st.caption(
        "Reference image = an empty/baseline shot of the same road. "
        "Sample image = the current traffic snapshot you want to evaluate. "
        "The app compares edge density between the two to estimate how congested the road is."
    )

st.divider()
with st.expander("ℹ️ How it works"):
    st.markdown("""
    1. Both images are converted to grayscale.
    2. Canny Edge Detection extracts edges (vehicle outlines, lane markings, etc.) from each.
    3. White (edge) pixels are counted in both images.
    4. Sample pixel count is compared to the reference count as a percentage.
    5. Green signal time is allocated based on that density percentage.
    """)

st.caption("Built by Kondrathi Shiva Shankar · [GitHub](https://github.com/ShivaShankar2026)")