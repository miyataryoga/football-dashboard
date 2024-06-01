import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
from streamlit_option_menu import option_menu
import os

current_path = os.getcwd()

def gauge_chart(value, texts):
    # Create the gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value,
        gauge={
            'axis': {'range': [0, 100]},
            'bar': {'color': "orange"},
        }
    ))

    # Customize layout
    fig.update_layout(
        font=dict(size=25)
    )

    # Add text annotation
    fig.add_annotation(x=0.5, y=0.2, text=texts, showarrow=False, font=dict(size=18, color="black"))

    # Display the gauge chart in Streamlit
    st.plotly_chart(fig)

# Define the path to your image
path_to_img = f'{current_path}\\image\\personal\\ryoga_miyata.jpg'
player_name = 'Ryoga Miyata'

# Add custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stApp {
        background-color: #ffffff;
    }
    </style>
    """, unsafe_allow_html=True)

# Title of the dashboard
#st.title("サッカー動作解析 ダッシュボート")

# Navigation menu
with st.sidebar:
    selected = option_menu("Menu", ["選手情報", "利き足評価", "逆足比較"],
                           icons=['person', 'bar-chart-line', 'bullseye'],
                           menu_icon="cast", default_index=0)

if selected == "選手情報":
    # 選手情報rmation
    st.markdown("<h1 style='text-align: center;'>選手情報</h1>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    with col1:
        st.image(path_to_img, width=280)
    with col2:
        st.markdown("<span style='font-size: 22px;'>選手名： 宮田龍芽</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 20px;'>ポジション： LSB</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 20px;'>生年月日： 3.25.2002 (22)</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 20px;'>身長/体重： 170cm/65kg</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 20px;'>出身地： 東京</span>", unsafe_allow_html=True)
        st.markdown("<span style='font-size: 20px;'>現所属チーム： Intel Biloba Tokyo</span>", unsafe_allow_html=True)

    # 直近の成績
    st.header("経歴")
    match_history_data = pd.DataFrame({
        'Team': ['ラスカル千駄木', 'FC.PROUD', '東海大高輪台', '芝浦工業大学', 'Intel Biloba Tokyo'],
        'Position': ['OMF', 'LSB', 'LSB', 'LWG', 'LSB'],
        'Season': ['2010-2014', '2014-2016', '2017-2019', '2020-2023', '2024-now'],
        'Goal': [12, 23, 32, 23, 4],
        'Assist': [10, 12, 20, 10, 5]
    })
    st.table(match_history_data)

elif selected == "利き足評価":
    # Market Value Graph
    st.markdown("<h1 style='text-align: center;'>利き足の評価結果</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center;'>評価： B (80)</h2>", unsafe_allow_html=True)

    user_name = 'kuwabara'
    date = '20240514'
    st.image(f'{current_path}\\image\\{user_name}\\{date}\\prefered_foot.png')

    market_value_data = pd.DataFrame({
        'Date': ['2021', '2022', '2023', '2024'],
        'Score': [0, 67, 76, 80]
    })
    fig, ax = plt.subplots()
    ax.plot(market_value_data['Date'], market_value_data['Score'], marker='o', color='orange')
    ax.set_title('Score Over Time')
    ax.set_xlabel('Year')
    ax.set_ylabel('Score (out of 100)')
    st.pyplot(fig)


elif selected == "逆足比較":
    # Radar Chart
    st.markdown("<h1 style='text-align: center;'>左右差比較</h1>", unsafe_allow_html=True)
    labels = ['Upper Body', 'Pelvis Stability', 'Back Swing', 'Power']
    values = [85, 78, 92, 70]

    
    fig_radar = go.Figure()
    fig_radar.add_trace(go.Scatterpolar(
        r=values,
        theta=labels,
        fill='toself',
        marker=dict(color='blue')
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100]
            ),
            angularaxis=dict(
                tickfont=dict(size=20)  # Adjust the size here
            )
        ),
        showlegend=False,
    )

    st.plotly_chart(fig_radar)

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        gauge_chart(values[1], 'Pelvis Stability')
    with col2:
        gauge_chart(values[0], 'Upper Body')
    with col3:
        gauge_chart(values[3], 'Power')
    with col4:
        gauge_chart(values[2], 'Back Swing')

    st.markdown("<h3>Upper Body (上半身の使い方)</h3>", unsafe_allow_html=True)
    st.text('サッカーにおいて、上半身の使い方はパスやシュートの精度に直結します。\nパスやシュート時には、上半身を適切に使うことで、ボールに対するコントロールとパワーを最大限に引き出すことができます。\n例えば、パスを出すときは肩の向きが非常に重要です。\n肩を狙った方向に向けることで、ボールが意図した方向に正確に飛んでいきます。\nまた、シュートの際には体重を前方に移動させることで、より強力なシュートを打つことが可能です。\nこれにより、相手ゴールキーパーが対応しにくい強烈なシュートが放てます。')
    
    st.markdown("<h3>Pelvis Stability (骨盤の安定性)</h3>", unsafe_allow_html=True)
    st.text('骨盤の安定性は、サッカーにおけるバランスとキックの精度に大きな影響を与えます。\nキックをする際に骨盤が安定していると、体重が均等に分配され、キックの力が効率的にボールに伝わります。\n例えば、フリーキックの際には骨盤を安定させることで、足の動きがスムーズになり、狙ったコースに正確にボールを飛ばすことができます。\nまた、ドリブル中の急な方向転換やスピードの変化に対しても、骨盤が安定していると素早く対応できます。')

    st.markdown("<h3>Back Swing (バックスウィングの大きさ)</h3>", unsafe_allow_html=True)
    st.text('バックスウィングの大きさは、シュートやパスの威力と精度に影響します。\nバックスウィングが適切であると、ボールに対するインパクトが最大化され、強力なシュートやロングパスが可能になります。\n例えば、強力なシュートを放つためには、しっかりとしたバックスウィングを取ることが重要です。\nしかし、短い距離のパスや近距離からのシュートでは、バックスウィングを小さくし、素早くボールを蹴ることで精度が上がります。')

    st.markdown("<h3>Power (キック力)</h3>", unsafe_allow_html=True)
    st.text('キック力は、シュートやロングパスの成功に不可欠な要素です。\n強力なキック力を持つことで、遠距離からのシュートやフィールド全体をカバーするパスが可能になります。')
    

# Run the app using: streamlit run dashboard.py
