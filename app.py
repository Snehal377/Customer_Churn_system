import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import joblib
import plotly.graph_objects as go
from sklearn.metrics import roc_curve, auc
import requests
from streamlit_lottie import st_lottie
import base64

def load_lottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_bg = load_lottie("https://assets2.lottiefiles.com/packages/lf20_jcikwtux.json")

def set_bg_local(image_file):
    import base64
    with open(image_file, "rb") as f:
        data = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{data}");
            background-size: cover ;   /* try cover OR 100% 100% */
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
           
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# analysis 
def set_gradient_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #050005 0%,
                #140010 40%,
                #2a0a25 70%,
                #3d1a35 100%
            );
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def pink_table_style():
    st.markdown("""
    <style>
    .pink-table {
        width: 100%;
        border-collapse: collapse;
        background: rgba(20, 0, 16, 0.8);
        color: white;
        border-radius: 12px;
        overflow: hidden;
        box-shadow: 0 0 20px rgba(255, 20, 147, 0.3);
    }

    .pink-table th {
        background: linear-gradient(90deg, #ff1493, #ff4da6);
        color: white;
        padding: 10px;
        text-align: left;
    }

    .pink-table td {
        padding: 10px;
        border-bottom: 1px solid rgba(255,255,255,0.1);
    }

    .pink-table tr:hover {
        background: rgba(255, 20, 147, 0.2);
    }
    </style>
    """, unsafe_allow_html=True)
#overview 
def set_overview_bg():
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(
            135deg,
            #000000 0%,
            #2a0f4f 25%,   /* Rich purple */
            #006b4f 70%,   /* Bright teal-green */
            #ff8c00 100%   /* Vibrant orange */
        );
        background-attachment: fixed;
        color: white;
    }
    </style>
    """, unsafe_allow_html=True) 
# predication 
def set_predication_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #000000 0%,      /* Pure black */
                #1a0f2e 30%,     /* Deep purple */
                #0f3d2e 65%,     /* Dark green */
                #3d1f0f 100%     /* Soft orange */
            );
            background-attachment: fixed;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

# predication charts 
st.markdown("""
<style>

/*  GLASS CHART CONTAINER */
.glass-chart {
    background: rgba(255, 255, 255, 0.05);
    padding: 20px;
    border-radius: 15px;
    backdrop-filter: blur(15px);

    /* MULTI COLOR GLOW */
    box-shadow: 
        0 0 15px rgba(0,255,150,0.3),
        0 0 25px rgba(140,0,255,0.3),
        0 0 35px rgba(255,140,0,0.3);

    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)    
# model 
def set_model_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #000000 10%,     /* Black */
                #1a0000 50%,    /* Dark Red */
                #660000 100%    /* Red */
            );
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# alert 
def set_alert_bg():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(
                135deg,
                #000000 10%,      
                #1a0033 50%, 
                #9d4edd 100%   
                    
            );
            background-attachment: fixed;
            
        }
        </style>
        """,
        unsafe_allow_html=True
    )
def netflix_card():
    st.markdown(
        """
        <style>
        .card {
            background: rgba(20, 0, 43, 0.7);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 0 20px rgba(157, 78, 221, 0.4);
            transition: 0.3s;
        }

        .card:hover {
            transform: scale(1.03);
            box-shadow: 0 0 30px rgba(157, 78, 221, 0.8);
        }
        </style>
        """,
        unsafe_allow_html=True
    ) 


def netflix_chart_style():
    plt.rcParams.update({
        "axes.facecolor": "#000000",
        "figure.facecolor": "#000000",
        "axes.edgecolor": "white",
        "axes.labelcolor": "white",
        "xtick.color": "white",
        "ytick.color": "white",
        "text.color": "white"
    })

def style_chart(fig):
    fig.update_layout(
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font_color="white",
        title_font=dict(color="#9d4edd", size=20),
    )

    fig.update_traces(
        marker=dict(color="#9d4edd"),
       
    )
    return fig

def style_table():
    st.markdown(
        """
        <style>
        .stDataFrame {
            background-color: rgba(20, 0, 43, 0.8);
            color: white;
            border-radius: 10px;
        }

        .stDataFrame th {
            background-color: #6a00f4 !important;
            color: white !important;
        }

        .stDataFrame td {
            background-color: rgba(0,0,0,0.6) !important;
            color: white !important;
        }
        </style>
        """,
        unsafe_allow_html=True
    ) 

def style_button():
    st.markdown(
        """
        <style>
        .stButton button {
            background-color: #6a00f4;
            color: white;
            border-radius: 10px;
            border: none;
            padding: 10px 20px;
        }

        .stButton button:hover {
            background-color: #9d4edd;
            box-shadow: 0 0 10px #9d4edd;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
# banner 

def set_top_banner(image_path):
    import base64
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(f"""
    <style>
    .main .block-container{{
        max-width:40%;
        padding-left: 0rem;
        padding-right:0rem;
    }}
    .top-banner {{
        width: 100%;
        height: 300px;

        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover; 
        background-repeat: no-repeat;
        background-position: center;
        margin-bottom: 20px;
        
    }}
    </style>

    <div class="top-banner"></div>
    """, unsafe_allow_html=True)

st.set_page_config(page_title="Churn Dashboard demo ", layout="wide")

# sider bar 
import base64

def set_sidebar_bg(image_path):
    import base64
    with open(image_path, "rb") as img:
        encoded = base64.b64encode(img.read()).decode()

    st.markdown(
        f"""
        <style>
        section[data-testid="stSidebar"] {{
            background: 
                linear-gradient(rgba(0,0,0,0), rgba(0,0,0,0)),
                url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# SIDEBAR
set_sidebar_bg("images/sidebar.jpg")
with st.sidebar:
    st.title("Telco Customer Churn System")
    st_lottie(
        lottie_bg,
        speed=1,
        loop=True,
        quality="high",
        height=150,
    )
    
    option = st.sidebar.radio(
        "Details",
        [ 
            "🏠 Overview",
            "🔮 Prediction",
            "📊 Analytics",
            "⚙️ Model Comparison",
            "🚨 Monitoring & Alerts"
        ]
    )

# PAGE 1: PREDICTION

if option == "🏠 Overview":

    set_overview_bg()
    set_top_banner("images/churns.jpg")

    st.markdown("""
    <style>

    /* GLASS CARD */
    .glass-card {
        background: rgba(255, 255, 255, 0.05);
        padding: 25px;
        border-radius: 15px;
        backdrop-filter: blur(12px);

        box-shadow: 
            0 0 15px rgba(0,255,150,0.2),
            0 0 25px rgba(140,0,255,0.2),
            0 0 35px rgba(255,140,0,0.2);

        margin-bottom: 20px;
        color: white;
    }

    /* KPI STYLE */
    .kpi-box {
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;
        font-weight: bold;

        border: 1px solid rgba(255,255,255,0.1);

        box-shadow: 
            0 0 10px rgba(0,255,150,0.3),
            0 0 20px rgba(140,0,255,0.3),
            0 0 30px rgba(255,140,0,0.3);
    }

    /* SECTION TITLE */
    .section-title {
        font-size: 22px;
        font-weight: bold;
        margin-bottom: 10px;
    }

    </style>
    """, unsafe_allow_html=True)

    #  TITLE
    st.title("📊 Customer Churn Dashboard")

    #  OVERVIEW CARD
    st.markdown("""
    <div class="glass-card">

    <div class="section-title">📌 Project Overview</div>
    Customer churn is a critical business problem. Retaining customers is more cost-effective than acquiring new ones.  
    This dashboard uses Machine Learning to predict churn risk and help businesses take proactive actions.

    <br>

    <div class="section-title">📂 Dataset Insights</div>
    • 7,043 telecom customers data  
    • Includes tenure, charges, contract, payment & demographics  

    <br>

    <div class="section-title">🤖 Models Used</div>
    • Logistic Regression  
    • Random Forest  
    • Gradient Boosting  
    • XGBoost  

    <br>

    <div class="section-title">🚀 Core Features</div>
    • ML-based Chrun Prediction System  
    • Interactive Analytics Dashboard
    • Model Comparison & Evaluation

    <br>
   
   <div class="section-title">🔥 Advanced Features (Production-Level)</div>

    ✨ <b>Real-Time Prediction API</b>  
    • FastAPI integration for live predictions  
    • Input: Customer ID / live data  
    • Output: Churn probability score  

    <br>

    📡 <b>Monitoring & Logging System</b>  
    • Prediction logs stored in CSV (simulation of pipeline)  
    • Track model outputs in real-time  
    • Risk distribution visualization  

    <br>

    🚨 <b>Business Rules Engine</b>  
    • If churn > 80% → High Risk  
    • Auto alert generation  
    • Priority-based customer segmentation  

    <br>

    📞 <b>CRM Integration (Simulated)</b>  
    • High-risk customers converted to follow-up tasks  
    • Sales/Retention team ready insights  

    <br>

    📊 <b>Advanced Visualization</b>  
    • KPI dashboards (Revenue, Churn Rate, Customers)  
    • Correlation heatmaps  
    • Feature importance analysis  
    • Interactive filtering  

    <br>

    ⚡ <b>Scalable Architecture (Simulation)</b>  
    • Built using modular pipeline approach  
    • Simulated real-time logging using CSV storage  
    • Architecture designed to support future integration with Kafka / BigQuery   

    </div>
    """, unsafe_allow_html=True)

    #  KPI CARDS
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="kpi-box">
            <h3>👥 Total Customers</h3>
            <h2>7043</h2>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="kpi-box">
            <h3>📉 Churn Rate</h3>
            <h2>26%</h2>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="kpi-box">
            <h3>💰 Revenue Impact</h3>
            <h2>High</h2>
        </div>
        """, unsafe_allow_html=True)

elif option == "🔮 Prediction":

    def set_predication_bg():
        st.markdown("""
        <style>

        .stApp {
            background: linear-gradient(
                135deg,
                #000000 0%,
                #1a0f2e 30%,
                #0f3d2e 65%,
                #3d1f0f 100%
            );
            background-attachment: fixed;
            color: white;
        }

        /*  Remove top padding */
        .block-container {
            padding-top: 1rem;
        }

        /*  Text visibility */
        h1, h2, h3, h4, h5, h6, p, label {
            color: white !important;
        }

        /*  Input fields */
        input, textarea {
            background-color: rgba(255,255,255,0.05) !important;
            color: white !important;
            border-radius: 8px !important;
            border: 1px solid rgba(255,255,255,0.2) !important;
        }

        /*  Selectbox */
        div[data-baseweb="select"] {
            background-color: rgba(255,255,255,0.05) !important;
            color: white !important;
        }

        /*  Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #00ff99, #8c00ff, #ff8c00);
            color: white;
            border-radius: 8px;
            border: none;
            font-weight: bold;
            box-shadow: 0 0 15px rgba(140,0,255,0.5);
        }

        /*  Dataframe */
        .stDataFrame {
            background-color: rgba(255,255,255,0.05);
            border-radius: 10px;
        }

        </style>
        """, unsafe_allow_html=True)

    set_predication_bg()

    #  TOP BANNER
    set_top_banner("images/Predication.jpg")

    st.title("🔮 Customer Churn Prediction")

    #  MODE SELECTION
    mode = st.radio(
        "Select Prediction Mode",
        ["By Customer ID (API)", "Manual Input (ML Model)"]
    )

    # ================= API MODE =================
    if mode == "By Customer ID (API)":

        customer_id = st.text_input("Enter Customer ID")

        if st.button("🚀 Predict via API"):

            if customer_id == "":
                st.warning("Please enter Customer ID")
            else:
                try:
                    url = f"http://127.0.0.1:8000/predict/{customer_id}"
                    response = requests.get(url)
                    data = response.json()

                    if "error" in data:
                        st.error(data["error"])
                    else:
                        prediction = data["prediction"]
                        probability = data["probability"]

                        st.markdown("### 📊 Prediction Result")

                        col1, col2 = st.columns(2)

                        with col1:
                            st.metric("Prediction", "Churn" if prediction==1 else "No Churn")

                        with col2:
                            st.metric("Probability", f"{probability:.2f}")

                        # Risk Level
                        if probability < 0.3:
                            st.success("🟢 Low Risk")
                        elif probability < 0.7:
                            st.warning("🟡 Medium Risk")
                        else:
                            st.error("🔴 High Risk")

                except:
                    st.error("⚠️ API not running! Start FastAPI first.")

    # ================= MANUAL MODE =================
    else:

        st.subheader("📝 Enter Customer Details")

        col1, col2 = st.columns(2)

        with col1:
            tenure = st.number_input("Tenure (months)", min_value=0)
            contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
            payment = st.selectbox("Payment Method", [
                "Electronic check", "Mailed check",
                "Bank transfer (automatic)", "Credit card (automatic)"
            ])

        with col2:
            monthly_charges = st.number_input("Monthly Charges", min_value=0.0)
            total_charges = st.number_input("Total Charges", min_value=0.0)
            internet = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
            gender = st.selectbox("Gender", ["Male", "Female"])

        if st.button("🚀 Predict Now"):

            try:
                model = joblib.load("churn_model.pkl")
                feature_names = joblib.load("feature_names.pkl")

                new_data = pd.DataFrame(0, index=[0], columns=feature_names)

                new_data["tenure"] = tenure
                new_data["MonthlyCharges"] = monthly_charges
                new_data["TotalCharges"] = total_charges

                if f"Contract_{contract}" in new_data.columns:
                    new_data[f"Contract_{contract}"] = 1

                if f"InternetService_{internet}" in new_data.columns:
                    new_data[f"InternetService_{internet}"] = 1

                if f"PaymentMethod_{payment}" in new_data.columns:
                    new_data[f"PaymentMethod_{payment}"] = 1

                if f"gender_{gender}" in new_data.columns:
                    new_data[f"gender_{gender}"] = 1

                prediction = model.predict(new_data)
                probability = model.predict_proba(new_data)[:, 1]
                
                st.markdown("### 📊 Prediction Result")
                #st.balloons()

                st.write(f"### Prediction: {'Churn' if prediction[0]==1 else 'No Churn'}")
                #st.balloons()
                st.write(f"### Probability: {probability[0]:.2f}")

                # Risk
                if probability[0] < 0.3:
                    st.success("🟢 Low Risk")
                elif probability[0] < 0.7:
                    st.warning("🟡 Medium Risk")
                else:
                    st.error("🔴 High Risk")

                #  GAUGE
                fig = go.Figure(go.Indicator(
                    mode="gauge+number",
                    value=probability[0]*100,
                    title={'text': "Churn Risk %"},
                    gauge={'axis': {'range': [0, 100]}}
                ))
                fig.update_layout(
                    paper_bgcolor='rgba(0,0,0,0)',   
                    plot_bgcolor='rgba(0,0,0,0)',   
                    font=dict(color='white'),
                )
                st.plotly_chart(fig, use_container_width=True)
               

                #  FEATURE IMPORTANCE
                importance = model.feature_importances_

                imp_df = pd.DataFrame({
                    "Feature": feature_names,
                    "Importance": importance
                }).sort_values(by="Importance", ascending=False).head(5)

                st.subheader("🔍 Top Factors Affecting Churn")
                st.markdown("""
                <style>
                .glass-table {
                    background: rgba(255, 255, 255, 0.05);
                    padding: 15px;
                    border-radius: 15px;
                    backdrop-filter: blur(12px);
                    box-shadow: 
                        0 0 15px rgba(0,255,150,0.3),
                        0 0 25px rgba(140,0,255,0.3),
                        0 0 35px rgba(255,140,0,0.3);

                    margin-top: 10px;
                }

                .glass-table table {
                    width: 100%;
                    border-collapse: collapse;
                    color: white;
                }
                .glass-table th {
                    background: rgba(255,255,255,0.1);
                    padding: 10px;
                    text-align: left;
                    font-weight: bold;
                }
                .glass-table td {
                    padding: 10px;
                    border-bottom: 1px solid rgba(255,255,255,0.1);
                }
                .glass-table tr:hover {
                    background: rgba(255,255,255,0.08);
                }
                </style>
                """, unsafe_allow_html=True)

                #  Convert DataFrame to HTML
                table_html = imp_df.to_html(index=False, escape=False)

                #  Wrap inside glass container
                st.markdown(f"""
                <div class="glass-table">
                {table_html}
                </div>
                """, unsafe_allow_html=True)

            except Exception as e:
                st.error(f"Error: {e}")

# PAGE 2: ANALYTICS

elif option == "📊 Analytics":
    set_gradient_bg()
    pink_table_style()

    st.markdown("""
    <style>

    .glass {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        box-shadow: 0 0 25px rgba(255, 20, 147, 0.2);
        color: white;
        margin-bottom: 20px;
    }

    .kpi-container {
        display: flex;
        gap: 25px;
        margin-top: 20px;
    }

    .kpi {
        flex: 1;
        background: liner-gradient(
            145deg,
            rgba(255,255,255,0.05),
            rgba(255,126,179,0.80)
        );
        padding: 20px;
        border-radius: 12px;
        text-align: center;
        color: white;

        border: 1px solid rgba(255, 20, 147, 0.3);

        box-shadow: 0 0 10px rgba(255, 77, 157, 0.4),
                    0 0 20px rgba(142, 58, 111, 0.3),
                    0 0 30px rgba(255,126,179,0.2);
    }

    .kpi-title {
        font-size: 14px;
        opacity: 0.7;
    }

    .kpi-value {
        font-size: 22px;
        font-weight: bold;
        margin-top: 5px;

    }

    </style>
    """, unsafe_allow_html=True)

    st.title("📊 Churn Analytics Dashboard")

    #  Load Data
    df = pd.read_csv("Telco_Cusomer_Churn.csv")

    #  Filters
    st.sidebar.subheader("🔍 Filters")

    gender_filter = st.sidebar.multiselect(
        "Gender", df["gender"].unique(), default=df["gender"].unique()
    )

    contract_filter = st.sidebar.multiselect(
        "Contract", df["Contract"].unique(), default=df["Contract"].unique()
    )

    internet_filter = st.sidebar.multiselect(
        "Internet", df["InternetService"].unique(), default=df["InternetService"].unique()
    )

    #Apply Filters
    filtered_df = df[
        (df["gender"].isin(gender_filter)) &
        (df["Contract"].isin(contract_filter)) &
        (df["InternetService"].isin(internet_filter))
    ]

    #  KPI Calculations
    total_customers = len(filtered_df)
    churn_count = filtered_df["Churn"].map({"Yes":1,"No":0}).sum()
    churn_rate = round((churn_count / total_customers) * 100, 2) if total_customers else 0
    active_customers = total_customers - churn_count
    revenue_loss = round(filtered_df.loc[filtered_df["Churn"]=="Yes","MonthlyCharges"].sum(), 2)

    #  KPI Cards 

    st.markdown("<div class='kpi-container'>", unsafe_allow_html=True)
    col1,col2,col3,col4= st.columns(4)
    with col1:
        st.markdown(f"""
        <div class='kpi'>
            <div class='kpi-title'>Total Customers</div>
            <div class='kpi-value'>{total_customers}</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class='kpi'>
            <div class='kpi-title'>Churn Rate</div>
            <div class='kpi-value'>{churn_rate}%</div>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class='kpi'>
            <div class='kpi-title'>Active Customers</div>
            <div class='kpi-value'>{active_customers}</div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div class='kpi'>
            <div class='kpi-title'>Revenue Loss</div>
            <div class='kpi-value'>${revenue_loss}</div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    #  Dataset Preview

    st.subheader("📄 Dataset Preview")
    st.markdown(
        filtered_df.head().to_html(classes="pink-table", index=False),
        unsafe_allow_html=True
    )

    # Basic Stats
  
    st.subheader("📌 Basic Statistics")

    stats_df = filtered_df.describe().reset_index()

    st.markdown(
        stats_df.to_html(classes="pink-table", index=False),
        unsafe_allow_html=True
    )
   
    #  Chart Theme 
    def style_chart(fig):
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )
        return fig

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Churn by Contract Types")
        data = filtered_df.groupby("Contract")["Churn"].value_counts().unstack().fillna(0)
        fig = px.bar(data, barmode="stack", color_discrete_sequence=["#ff4d9d","#ff7eb3"])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    with col2:
        st.subheader("Churn by Payment Methods")
        data = filtered_df.groupby("PaymentMethod")["Churn"].value_counts().unstack().fillna(0)
        fig = px.bar(data, barmode="stack", color_discrete_sequence=["#ff4d9d","#ff7eb3"])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Customer Tenure Distribution")
        fig = px.histogram(filtered_df, x="tenure", nbins=20, color_discrete_sequence=["#8e3a6f"])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    with col4:
        st.subheader("Monthly Charges Trend")
        avg = filtered_df.groupby("tenure")["MonthlyCharges"].mean().reset_index()
        fig = px.line(avg, x="tenure", y="MonthlyCharges", color_discrete_sequence=["#ff7eb3"])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    col5, col6 = st.columns(2)

    with col5:
        st.subheader("Churn Distribution")
        churn_counts = filtered_df["Churn"].value_counts().reset_index()
        churn_counts.columns = ["Churn","Count"]
        fig = px.bar(churn_counts, x="Churn", y="Count", color_discrete_sequence=["#ff4d9d","#ff7eb3"])
        st.plotly_chart(style_chart(fig), use_container_width=True)

    with col6:
        st.subheader("Monthly Charges Distribution")
        fig = px.histogram(filtered_df, x="MonthlyCharges", nbins=20, color_discrete_sequence=["#8e3a6f"])
        st.plotly_chart(style_chart(fig), use_container_width=True)
    
    col1, col2 = st.columns(2)

    def style_chart(fig):
        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
           font_color="white"
        )
        return fig

    with col1:
        st.subheader("🔥 Correlation Heatmap")
        
        corr = filtered_df.corr(numeric_only=True)

        fig4 = px.imshow(
            corr,
            text_auto=True,
            color_continuous_scale=[
                "#140010",  
                "#8e3a6f",   
                "#ff7eb3"  
            ]
        )

        st.plotly_chart(style_chart(fig4), use_container_width=True)

    with col2:
        st.subheader("💵 Total Charges Distribution")

        fig = px.box(
            filtered_df,
            y="TotalCharges",
            color_discrete_sequence=["#ff4d9d"]
        )

        fig.update_traces(
            marker=dict(
                color="#ff7eb3",
                line=dict(color="#8e3a6f", width=2)
            )
        )
        st.plotly_chart(style_chart(fig), use_container_width=True)

elif option == "⚙️ Model Comparison":

    st.markdown("""
    <style>
    /* Netflix Background */
    .stApp {
        background: linear-gradient(135deg, #000000, #1a0000, #330000);
    }

    /* Glass Card */
    .glass {
        background: rgba(255, 255, 255, 0.08);
        padding: 20px;
        border-radius: 15px;
        backdrop-filter: blur(12px);
        margin-bottom: 20px;
        box-shadow: 0 4px 25px rgba(0,0,0,0.6);
        color: white;
    }

    /* KPI Container */
    .kpi-container {
        display: flex;
        gap: 25px;  /*  more spacing between cards */
        margin-top: 25px;
    }

    /* KPI Card */
    .kpi {
        flex: 1;
        background: rgba(255,255,255,0.05);
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        color: white;
        font-weight: bold;

        /*  CLEAR BORDER */
        border: 2px solid rgba(255,255,255,0.2);

        /*  GLOW */
        box-shadow: 0 0 12px rgba(229,9,20,0.5);

        /* Prevent merging look */
        min-width: 120px;
    }

    /* Optional: inner text styling */
    .kpi span {
        display: block;
        font-size: 14px;
        opacity: 0.8;
    }

    .kpi strong {
        font-size: 20px;
        color: #ffffff;
    }

    /* Best Model Highlight */
    .best-model {
        background: linear-gradient(90deg, #E50914, #ff4b2b);
        padding: 12px;
        border-radius: 10px;
        color: white;
        font-weight: bold;
        text-align: center;
        box-shadow: 0 0 15px rgba(229,9,20,0.8);
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🤖 Model Performance Dashboard")

    try:
        metrics = joblib.load("model_metrics.pkl")
        df_metrics = pd.DataFrame(metrics).T

        #  Best Model
        best_model = df_metrics["ROC"].idxmax()
        st.markdown(
            f"<div class='best-model'>🏆 Best Model: {best_model}</div>",
            unsafe_allow_html=True
        )
        #  Model Selection
        model_choice = st.selectbox(
            "Select Model",
            df_metrics.index.tolist()
        )

        selected_data = df_metrics.loc[model_choice]

        st.markdown(f"<div class='glass'><h3>📌 {model_choice} Performance</h3></div>", unsafe_allow_html=True)
        
        st.subheader("🎯 Model Strength (ROC-AUC)")
        
        #  Gauge Chart
        fig = go.Figure(go.Indicator(
            mode="gauge+number",
            value=selected_data["ROC"] * 100,
            title={'text': "ROC-AUC Score"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "#E50914"}, 
                'steps': [
                    {'range': [0, 50], 'color': "#444"},
                    {'range': [50, 75], 'color': "#888"},
                    {'range': [75, 100], 'color': "#E50914"}
                ]
            }
        ))

        fig.update_layout(paper_bgcolor="rgba(0,0,0,0)", font_color="white")
        st.plotly_chart(fig, use_container_width=True)

        #  KPI Cards
        col1, col2, col3, col4 = st.columns(4)
        st.markdown("<div class ='kpi-container'>",unsafe_allow_html=True)
        with col1:
            st.markdown(f"<div class='kpi'><span>Accuracy</span><strong>{selected_data['Accuracy']:.2f}</strong></div>", unsafe_allow_html=True)
        with col2:
            st.markdown(f"<div class='kpi'><span>Precision</span><strong>{selected_data['Precision']:.2f}</strong></div>", unsafe_allow_html=True)
        with col3:
            st.markdown(f"<div class='kpi'><span>Recall</span><strong>{selected_data['Recall']:.2f}</strong></div>", unsafe_allow_html=True)
        with col4:
            st.markdown(f"<div class='kpi'><span>F1 Score</span><strong>{selected_data['F1']:.2f}</strong></div>", unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)

        #  Metrics Bar Chart
        st.markdown("<div class='glass'><h4>📊 Model Metrics</h4></div>", unsafe_allow_html=True)

        chart_df = pd.DataFrame({
            "Metric": ["Accuracy", "Precision", "Recall", "F1", "ROC"],
            "Value": [
                selected_data["Accuracy"],
                selected_data["Precision"],
                selected_data["Recall"],
                selected_data["F1"],
                selected_data["ROC"]
            ]
        })

        fig = px.bar(
            chart_df,
            x="Metric",
            y="Value",
            text="Value",
            color="Value",
            title=f"{model_choice} Performance",
            color_continuous_scale="reds"
        )

        fig.update_layout(
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font_color="white"
        )

        st.plotly_chart(fig, use_container_width=True)

        #  ROC Curve
        st.markdown("<div class='glass'><h4>📈 ROC Curve</h4></div>", unsafe_allow_html=True)

        try:
            models = joblib.load("all_models.pkl")
            model = models[model_choice]

            X_test = joblib.load("X_test.pkl")
            y_test = joblib.load("y_test.pkl")

            y_prob = model.predict_proba(X_test)[:, 1]

            fpr, tpr, _ = roc_curve(y_test, y_prob)
            roc_auc = auc(fpr, tpr)

            fig = go.Figure()

            fig.add_trace(go.Scatter(
                x=fpr,
                y=tpr,
                mode='lines',
                name=f"{model_choice} (AUC={roc_auc:.2f})",
                line=dict(color="#E50914", width=3)
            ))

            fig.add_trace(go.Scatter(
                x=[0, 1],
                y=[0, 1],
                mode='lines',
                line=dict(dash='dash', color="gray"),
                name="Random"
            ))

            fig.update_layout(
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font_color="white",
                xaxis_title="False Positive Rate",
                yaxis_title="True Positive Rate",
                title=f"ROC Curve - {model_choice}"
            )

            st.plotly_chart(fig, use_container_width=True)

        except Exception as e:
            st.error(f"ROC Error: {e}")

    except Exception as e:
        st.error(f"Error: {e}")

# ================= MONITORING PAGE =================
    
elif option == "🚨 Monitoring & Alerts":
    set_alert_bg()
    style_table()
    netflix_card()
    style_button()


    st.title("🚨 Real-Time Monitoring Dashboard")

    col1, col2, col3 = st.columns(3)

    # ================= LOAD FILES =================
    try:
        logs = pd.read_csv("prediction_logs.csv")
    except:
        logs = pd.DataFrame()

    try:
        alerts = pd.read_csv("alerts.csv")
    except:
        alerts = pd.DataFrame()

    try:
        crm = pd.read_csv("crm_tasks.csv")
    except:
        crm = pd.DataFrame()

    # ================= KPI =================
    with col1:
        st.markdown(f"""
        <div class ="card">
            <h3>Total Predictions</h3>
            <h1>{len(logs)}</h1>
        </div>
        """,unsafe_allow_html=True)
        

    with col2:
        st.markdown(f"""
        <div class ="card">
            <h3>High Risk Alerts</h3>
            <h1>{len(alerts)}</h1>
        </div>
        """,unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class ="card">
            <h3>High CRM Tasks</h3>
            <h1>{len(crm)}</h1>
        </div>
        """,unsafe_allow_html=True)
        

    st.markdown("---")

    # ================= LOGS =================

    st.subheader("📊 Prediction Logs")

    if not logs.empty:

        st.markdown("""
        <style>
        .netflix-table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(20, 0, 43, 0.7);
            color: white;
            border-radius: 10px;
            overflow: hidden;
        }

        .netflix-table th {
            background-color: #6a00f4;
            padding: 10px;
            text-align: left;
        }

        .netflix-table td {
            padding: 10px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .netflix-table tr:hover {
            background-color: rgba(157, 78, 221, 0.2);
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(
            logs.tail(10).to_html(classes="netflix-table", index=False),
            unsafe_allow_html=True
        )

        fig = px.histogram(
            logs,
            x="probability",
            nbins=20,
            title="Risk Distribution"
        )
        fig = style_chart(fig)

        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("No logs available yet")

    # ================= ALERTS =================
    st.subheader("🚨 High Risk Customers")

    if not alerts.empty:
        st.markdown(
            alerts.tail(10).to_html(classes="netflix-table", index=False),
            unsafe_allow_html=True
        )

    else:
        st.markdown("""
        <div style="
            background: rgba(20, 0, 43, 0.7);
            padding: 15px;
            border-radius: 10px;
            color: #9d4edd;
            text-align: left;
            font-weight: bold;">
           ✅ No high-risk customers
        </div>
        """, unsafe_allow_html=True)

    # ================= CRM =================

    st.subheader("📞 CRM Follow-ups")

    if not crm.empty:
        st.markdown("""
        <style>
        .netflix-table {
            width: 100%;
            border-collapse: collapse;
            background: rgba(20, 0, 43, 0.7);
            color: white;
            border-radius: 10px;
            overflow: hidden;
        }

        .netflix-table th {
            background-color: #6a00f4;
            padding: 10px;
            text-align: left;
        }

        .netflix-table td {
            padding: 10px;
            border-bottom: 1px solid rgba(255,255,255,0.1);
        }

        .netflix-table tr:hover {
            background-color: rgba(157, 78, 221, 0.2);
        }
        </style>
        """, unsafe_allow_html=True)

        st.markdown(
            crm.tail(10).to_html(classes="netflix-table", index=False),
            unsafe_allow_html=True
        )
    else:
        st.info("No CRM tasks yet")        