import streamlit as st 
import pandas as pd 

st.title('mai mai python第一階段成果')
st.markdown('Machine Learning：')


contact_option = st.sidebar.selectbox(
    '選擇你想看的預測模型結果',
    ('Preliminary results','Logistic regression', 'Random forest', 'XGBost','Model Performance Comparison')  # 確保括號正確閉合
)

if contact_option == 'Preliminary results':
    table1, table2= st.tabs(['Sex','Age'])
   
    with table1:
        st.header('Sex distribution')
        st.image('gender_distribution.png')
        st.write('0=女性 1=男性')
        
    with table2:
        st.header('Age distribution')
        st.image('age_distribution.png')
        st.write("這張圖展示了年齡分佈，大多數人群集中在30到50歲之間")
    
    table1, table2= st.tabs(['Age vs. Max Heart Rate','Chest Pain Type vs. Heart Disease'])

    with table1:
        st.header('Age vs. Max Heart Rate')
        st.image('age_vs_thalach.png')
        st.write('從此散佈圖中可以觀察到，隨著年齡的增長，最大心率顯著下降，'
         '且患有心臟病的患者（橙色點）往往分佈在較低的心率範圍內。表示年齡和'
         '最大心率與心臟病之間存在一定的關聯性，特別是老年人和較低的最大心率群體'
         '可能更容易患心臟病。')

    with table2:
        st.header('Chest Pain Type vs. Heart Disease')
        st.image('cp_vs_heart_disease.png')
        st.write('從此長條圖中，可以明顯看到胸痛類型與心臟病之間的強烈相關性，'
         '特別是 cp=2（非典型心絞痛）和 cp=1（心絞痛）的患者更容易被診斷為心臟病（橙色）。'
         '表示胸痛類型是一個重要的預測變數。')

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header('🌟Correlation Matrix')
    st.image('correlation_matrix.png')
    st.write('⭐ 通過correlation matrix可以進一步確認某些特徵與心臟病的相關性：'
         '胸痛類型 (cp) 與 心臟病 (target) 的相關性最高，達到了 0.43，表示一個重要的預測因素。')

    st.write('⭐ 最大心率 (thalach) 也與心臟病有較高的相關性（0.42），支持了散佈圖中的觀察結果。')

    st.write('⭐ 運動誘發的心絞痛 (exang) 和 ST 段變化 (oldpeak) 也對心臟病具有一定的影響，相關性分別為 -0.44 和 -0.43')

    if st.button('Show Summary'):
        st.markdown("<hr>", unsafe_allow_html=True)  # 添加一條分隔線
        st.header("Summary")  # 顯示總結標題
        st.write('根據 EDA 的結果，我們可以初步推斷，以下特徵對於預測心臟病具有較高的影響力：')

        st.write('1. **胸痛類型 (cp)**：與心臟病有最強的相關性。')

        st.write('2. **最大心率 (thalach)**：老年患者和較低的最大心率群體更容易患病。')

        st.write('3. **運動誘發的心絞痛 (exang) 和 ST 段變化 (oldpeak)**：這些特徵也具有顯著的影響。')

        st.write('4. **性別 (sex)**：男性患者的患病率相對更高（但也可能因為佔比較高原因）。')
    
if contact_option == 'Logistic regression':
    # 顯示 Logistic Regression 結果
    st.header('Logistic Regression Result')

    # 顯示 Logistic Regression 的圖片
    st.image('Logistic_Regression_Confusion_Matrix.png')  # 替換成您的圖片路徑
    
    # 顯示 Logistic Regression 的評估結果
    st.write('**Precision:** 0.87')
    st.write('**Recall:** 0.86')
    st.write('**F1-score:** 0.86')
    st.write('**Support:** 32')
    st.write('**Accuracy:** 0.85')  # 注意這裡讓 Accuracy 用紅色顯示

    # 用紅色顯示 Accuracy
    st.markdown('<span style="color:red;">Accuracy: 0.85</span>', unsafe_allow_html=True)

elif contact_option == 'Random forest':
    # 顯示 Random Forest 結果
    st.header('Random Forest Result')

    # 顯示 Random Forest 的圖片（可以替換為您自己的圖片）
    st.image('Random_Forest_Confusion_Matrix.png')  # 替換成您的圖片路徑
    
    # 顯示 Random Forest 的評估結果
    st.write('**Precision:** 0.84')
    st.write('**Recall:** 0.84')
    st.write('**F1-score:** 0.84')
    st.write('**Support:** 29')
    st.write('**Accuracy:** 0.84')

elif contact_option == 'XGBost':
    # 顯示 XGBoost 結果
    st.header('XGBoost Result')

    # 顯示 XGBoost 的圖片（可以替換為您自己的圖片）
    st.image('XGBoost_Confusion_Matrix.png')  # 替換成您的圖片路徑
    
    # 顯示 XGBoost 的評估結果
    st.write('**Precision:** 0.86')
    st.write('**Recall:** 0.78')
    st.write('**F1-score:** 0.82')
    st.write('**Support:** 32')
    st.write('**Accuracy:** 0.82')   

if contact_option == 'Model Performance Comparison':
    st.header('🔍 Model Performance Comparison')

    st.markdown("""
    根據不同模型的評估結果，我們比較了 Logistic Regression (LR)、Random Forest (RF) 和 XGBoost 的性能。以下是各模型的主要評估指標：

    - **LR** 在所有評估指標中表現最佳，特別是在精確率（0.87）和 F1 分數（0.86）方面，顯示出其對正類預測的高度準確性和穩定性。
    - **RF** 的性能略低於 LR，但在所有指標中也顯示了不錯的結果，尤其是在準確率（0.84）方面。
    - **XGBoost** 的精確率（0.86）相當不錯，但其召回率（0.78）顯示出在識別正類樣本方面有所不足，這可能由於假負例（7）較多造成。
    """)

     # 顯示表格來比較模型的性能
    data = {
        'Metric': ['Precision', 'Recall', 'F1-score', 'Support', 'Accuracy'],
        'Logistic Regression (LR)': [0.87, 0.86, 0.86, 32.0, 0.85],
        'Random Forest (RF)': [0.84, 0.84, 0.84, 29.0, 0.84],
        'XGBoost': [0.86, 0.78, 0.82, 32.0, 0.82]
    }

    # 使用 round 函數來去除多餘的零
    df = pd.DataFrame(data)
    df = df.round(2)  # 四捨五入到兩位小數

    # 顯示格式化後的表格
    st.table(df)  # 顯示表格

    if st.button('Show Confusion Matrices'):
        st.subheader('Confusion Matrix for Each Model')

        # 創建三個並排的列
        col1, col2, col3 = st.columns(3)

        with col1:
            # 顯示 Logistic Regression 的混淆矩陣圖
            st.image('Logistic_Regression_Confusion_Matrix.png', caption='Logistic Regression')

        with col2:
            # 顯示 Random Forest 的混淆矩陣圖
            st.image('Random_Forest_Confusion_Matrix.png', caption='Random Forest')

        with col3:
            # 顯示 XGBoost 的混淆矩陣圖
            st.image('XGBoost_Confusion_Matrix.png', caption='XGBoost')
