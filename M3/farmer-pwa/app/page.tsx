"use client";

import { ChangeEvent, useEffect, useState } from "react";

type SoilData = {
  nitrogen: string;
  phosphorus: string;
  potassium: string;
  ph: string;
  moisture: string;
  organicMatter: string;
};

type Results = {
  healthScore: number;
  healthStatus: string;

  soilValues: {
    nitrogen: number;
    phosphorus: number;
    potassium: number;
    ph: number;
    moisture: number;
    organicMatter: number;
  };

  conditions: {
    nitrogen: string;
    phosphorus: string;
    potassium: string;
    ph: string;
    moisture: string;
    organicMatter: string;
  };

  crops: string[];
  recommendations: string[];
  soilType: string;

  soilConfidence: number;
};

export default function Home() {
  const [language, setLanguage] = useState("English");

  const translations = {
    English: {
      title: "AI-Powered Soil Analysis",
      welcome: "Welcome Farmer 👨‍🌾",
      analyze: "Analyze Soil 🌱",
      newAnalysis: "New Analysis",
      analyzing: "Analyzing Soil...",
      history: "Analysis History 📋",
      soilImage: "Soil Image",
      removeImage: "Remove Image",
      soilParameters: "Soil Parameters",
      soilHealth: "Soil Health",
      conditions: "Nutrient & Soil Conditions",
      recommendations: "Farmer Recommendations 🧑‍🌾",
      crops: "Suitable Crops 🌾",
      footer: "AI-Powered Soil Analytics System",
      welcomeText:
        "Enter your soil information to get soil-health insights, recommendations and suitable crops.",
      imageErrorType: "Please upload a JPG or PNG image.",
      imageErrorSize: "Image size must be less than 5 MB.",
      nitrogen: "Nitrogen",
      phosphorus: "Phosphorus",
      potassium: "Potassium",
      moisture: "Moisture",
      organicMatter: "Organic Matter",
      olderAnalysis: "Older analysis",
      remove: "Remove Image",
      noHistory: "No analysis history yet.",
    },

    Hindi: {
      title: "AI-संचालित मिट्टी विश्लेषण",
      welcome: "किसान जी, आपका स्वागत है 👨‍🌾",
      analyze: "मिट्टी का विश्लेषण करें 🌱",
      newAnalysis: "नया विश्लेषण",
      analyzing: "मिट्टी का विश्लेषण हो रहा है...",
      history: "विश्लेषण इतिहास 📋",
      soilImage: "मिट्टी की तस्वीर",
      removeImage: "तस्वीर हटाएँ",
      soilParameters: "मिट्टी के पैरामीटर",
      soilHealth: "मिट्टी का स्वास्थ्य",
      conditions: "पोषक तत्व और मिट्टी की स्थिति",
      recommendations: "किसान के लिए सुझाव 🧑‍🌾",
      crops: "उपयुक्त फसलें 🌾",
      footer: "AI-संचालित मिट्टी विश्लेषण प्रणाली",
      welcomeText:
        "मिट्टी की जानकारी दर्ज करें और मिट्टी के स्वास्थ्य, सुझाव और उपयुक्त फसलों की जानकारी प्राप्त करें।",
      imageErrorType: "कृपया JPG या PNG तस्वीर अपलोड करें।",
      imageErrorSize: "तस्वीर का आकार 5 MB से कम होना चाहिए।",
      nitrogen: "नाइट्रोजन",
      phosphorus: "फॉस्फोरस",
      potassium: "पोटैशियम",
      moisture: "नमी",
      organicMatter: "जैविक पदार्थ",
      olderAnalysis: "पुराना विश्लेषण",
      remove: "तस्वीर हटाएँ",
      noHistory: "अभी कोई विश्लेषण इतिहास नहीं है।",
    },

    Kannada: {
      title: "AI-ಚಾಲಿತ ಮಣ್ಣಿನ ವಿಶ್ಲೇಷಣೆ",
      welcome: "ರೈತರಿಗೆ ಸ್ವಾಗತ 👨‍🌾",
      analyze: "ಮಣ್ಣನ್ನು ವಿಶ್ಲೇಷಿಸಿ 🌱",
      newAnalysis: "ಹೊಸ ವಿಶ್ಲೇಷಣೆ",
      analyzing: "ಮಣ್ಣಿನ ವಿಶ್ಲೇಷಣೆ ನಡೆಯುತ್ತಿದೆ...",
      history: "ವಿಶ್ಲೇಷಣೆ ಇತಿಹಾಸ 📋",
      soilImage: "ಮಣ್ಣಿನ ಚಿತ್ರ",
      removeImage: "ಚಿತ್ರವನ್ನು ತೆಗೆದುಹಾಕಿ",
      soilParameters: "ಮಣ್ಣಿನ ನಿಯತಾಂಕಗಳು",
      conditions: "ಪೋಷಕಾಂಶ ಮತ್ತು ಮಣ್ಣಿನ ಸ್ಥಿತಿಗಳು",
      recommendations: "ರೈತರಿಗೆ ಸಲಹೆಗಳು 🧑‍🌾",
      crops: "ಸೂಕ್ತ ಬೆಳೆಗಳು 🌾",
      footer: "AI-ಚಾಲಿತ ಮಣ್ಣಿನ ವಿಶ್ಲೇಷಣಾ ವ್ಯವಸ್ಥೆ",
      welcomeText:
        "ಮಣ್ಣಿನ ಮಾಹಿತಿಯನ್ನು ನಮೂದಿಸಿ ಮತ್ತು ಮಣ್ಣಿನ ಆರೋಗ್ಯ, ಸಲಹೆಗಳು ಹಾಗೂ ಸೂಕ್ತ ಬೆಳೆಗಳ ಮಾಹಿತಿಯನ್ನು ಪಡೆಯಿರಿ.",
      imageErrorType: "ದಯವಿಟ್ಟು JPG ಅಥವಾ PNG ಚಿತ್ರವನ್ನು ಅಪ್‌ಲೋಡ್ ಮಾಡಿ.",
      imageErrorSize: "ಚಿತ್ರದ ಗಾತ್ರ 5 MB ಗಿಂತ ಕಡಿಮೆ ಇರಬೇಕು.",
      nitrogen: "ನೈಟ್ರೋಜನ್",
      phosphorus: "ಫಾಸ್ಫರಸ್",
      potassium: "ಪೊಟ್ಯಾಸಿಯಮ್",
      moisture: "ತೇವಾಂಶ",
      organicMatter: "ಸಾವಯವ ಪದಾರ್ಥ",
      olderAnalysis: "ಹಳೆಯ ವಿಶ್ಲೇಷಣೆ",
      remove: "ಚಿತ್ರವನ್ನು ತೆಗೆದುಹಾಕಿ",
      noHistory: "ಇನ್ನೂ ಯಾವುದೇ ವಿಶ್ಲೇಷಣೆ ಇತಿಹಾಸವಿಲ್ಲ.",
    },
  };

  const t =
    translations[language as keyof typeof translations] ||
    translations.English;

  const [imagePreview, setImagePreview] = useState<string | null>(null);
  const [imageFile, setImageFile] = useState<File | null>(null);
  const [imageError, setImageError] = useState("");

  const [formData, setFormData] = useState<SoilData>({
    nitrogen: "",
    phosphorus: "",
    potassium: "",
    ph: "",
    moisture: "",
    organicMatter: "",
  });

  const [formErrors, setFormErrors] = useState<Record<string, string>>({});
  const [results, setResults] = useState<Results | null>(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [analysisError, setAnalysisError] = useState("");
  const [history, setHistory] = useState<Results[]>([]);
  const [showAllHistory, setShowAllHistory] = useState(false);

  useEffect(() => {
    const savedHistory = localStorage.getItem("soilAnalysisHistory");

    if (savedHistory) {
      try {
        setHistory(JSON.parse(savedHistory));
      } catch {
        setHistory([]);
      }
    }
  }, []);

  const handleInputChange = (
    e: ChangeEvent<HTMLInputElement>
  ) => {
    const { name, value } = e.target;

    setFormData((previous) => ({
      ...previous,
      [name]: value,
    }));
  };

  const handleImageChange = (
    e: ChangeEvent<HTMLInputElement>
  ) => {
    const file = e.target.files?.[0];

    setImageError("");

    if (!file) {
      return;
    }

    const allowedTypes = [
      "image/jpeg",
      "image/jpg",
      "image/png",
    ];

    if (!allowedTypes.includes(file.type)) {
      setImageError(t.imageErrorType);
      return;
    }

    if (file.size > 5 * 1024 * 1024) {
      setImageError(t.imageErrorSize);
      return;
    }

    setImagePreview(URL.createObjectURL(file));
    setImageFile(file);
  };

  const validateForm = () => {
    const errors: Record<string, string> = {};

    const n = Number(formData.nitrogen);
    const p = Number(formData.phosphorus);
    const k = Number(formData.potassium);
    const ph = Number(formData.ph);
    const moisture = Number(formData.moisture);
    const organicMatter = Number(formData.organicMatter);

    if (formData.nitrogen === "" || n < 0) {
      errors.nitrogen = "Enter a valid nitrogen value.";
    }

    if (formData.phosphorus === "" || p < 0) {
      errors.phosphorus = "Enter a valid phosphorus value.";
    }

    if (formData.potassium === "" || k < 0) {
      errors.potassium = "Enter a valid potassium value.";
    }

    if (formData.ph === "" || ph < 0 || ph > 14) {
      errors.ph = "pH must be between 0 and 14.";
    }

    if (
      formData.moisture === "" ||
      moisture < 0 ||
      moisture > 100
    ) {
      errors.moisture = "Moisture must be between 0 and 100.";
    }

    if (
      formData.organicMatter === "" ||
      organicMatter < 0
    ) {
      errors.organicMatter =
        "Enter a valid organic matter value.";
    }

    setFormErrors(errors);

    return Object.keys(errors).length === 0;
  };

  /* =========================
     TRANSLATION FUNCTIONS
     ========================= */

  const translateHealthStatus = (status: string) => {
    if (language === "Hindi") {
      if (status === "Healthy") return "स्वस्थ";
      if (status === "Moderately Healthy")
        return "मध्यम रूप से स्वस्थ";
      if (status === "Needs Improvement")
        return "सुधार की आवश्यकता";
      if (status === "Poor") return "खराब";
    }

    if (language === "Kannada") {
      if (status === "Healthy") return "ಆರೋಗ್ಯಕರ";
      if (status === "Moderately Healthy")
        return "ಮಧ್ಯಮ ಆರೋಗ್ಯಕರ";
      if (status === "Needs Improvement")
        return "ಸುಧಾರಣೆ ಅಗತ್ಯ";
      if (status === "Poor") return "ಕಳಪೆ";
    }

    return status;
  };
  const translateSoilType = (soilType: string) => {
  if (language === "Hindi") {
    const hindiSoilTypes: Record<string, string> = {
      Alluvial: "जलोढ़ मिट्टी",
      Arid: "शुष्क मिट्टी",
      Black: "काली मिट्टी",
      Laterite: "लेटराइट मिट्टी",
      Mountain: "पर्वतीय मिट्टी",
      Red: "लाल मिट्टी",
      Yellow: "पीली मिट्टी",
    };

    return hindiSoilTypes[soilType] || soilType;
  }

  if (language === "Kannada") {
    const kannadaSoilTypes: Record<string, string> = {
      Alluvial: "ಮೆಕ್ಕಲು ಮಣ್ಣು",
      Arid: "ಶುಷ್ಕ ಮಣ್ಣು",
      Black: "ಕಪ್ಪು ಮಣ್ಣು",
      Laterite: "ಲ್ಯಾಟರೈಟ್ ಮಣ್ಣು",
      Mountain: "ಪರ್ವತ ಮಣ್ಣು",
      Red: "ಕೆಂಪು ಮಣ್ಣು",
      Yellow: "ಹಳದಿ ಮಣ್ಣು",
    };

    return kannadaSoilTypes[soilType] || soilType;
  }

  return soilType;
};
  const translateCondition = (condition: string) => {
    if (language === "Hindi") {
      if (condition === "Low") return "कम";
      if (condition === "High") return "अधिक";
      if (condition === "Adequate") return "पर्याप्त";
      if (condition === "Suitable") return "उपयुक्त";
      if (condition === "Acidic") return "अम्लीय";
      if (condition === "Alkaline") return "क्षारीय";
    }

    if (language === "Kannada") {
      if (condition === "Low") return "ಕಡಿಮೆ";
      if (condition === "High") return "ಹೆಚ್ಚು";
      if (condition === "Adequate") return "ಸಾಕಷ್ಟು";
      if (condition === "Suitable") return "ಸೂಕ್ತ";
      if (condition === "Acidic") return "ಆಮ್ಲೀಯ";
      if (condition === "Alkaline") return "ಕ್ಷಾರೀಯ";
    }

    return condition;
  };

  const translateRecommendation = (
    recommendation: string
  ) => {
    if (language === "Hindi") {
      if (
        recommendation.startsWith(
          "Nitrogen supplementation"
        )
      )
        return "नाइट्रोजन की पूर्ति की आवश्यकता हो सकती है। मिट्टी परीक्षण और फसल की आवश्यकताओं के अनुसार मार्गदर्शन का पालन करें।";

      if (
        recommendation.startsWith(
          "Avoid additional nitrogen"
        )
      )
        return "जब तक मिट्टी परीक्षण या फसल की आवश्यकताओं के अनुसार सलाह न दी जाए, अतिरिक्त नाइट्रोजन से बचें।";

      if (
        recommendation.startsWith(
          "Nitrogen level is adequate"
        )
      )
        return "नाइट्रोजन का स्तर पर्याप्त है। वर्तमान मिट्टी प्रबंधन बनाए रखें।";

      if (
        recommendation.startsWith(
          "Phosphorus supplementation"
        )
      )
        return "मिट्टी परीक्षण और फसल की आवश्यकताओं के आधार पर फॉस्फोरस की पूर्ति की आवश्यकता हो सकती है।";

      if (
        recommendation.startsWith(
          "Avoid additional phosphorus"
        )
      )
        return "जब तक सलाह न दी जाए, अतिरिक्त फॉस्फोरस से बचें।";

      if (
        recommendation.startsWith(
          "Phosphorus level is adequate"
        )
      )
        return "फॉस्फोरस का स्तर पर्याप्त है।";

      if (
        recommendation.startsWith(
          "Potassium supplementation"
        )
      )
        return "मिट्टी परीक्षण के आधार पर पोटैशियम की पूर्ति की आवश्यकता हो सकती है।";

      if (
        recommendation.startsWith(
          "Avoid additional potassium"
        )
      )
        return "जब तक सलाह न दी जाए, अतिरिक्त पोटैशियम से बचें।";

      if (
        recommendation.startsWith(
          "Potassium level is adequate"
        )
      )
        return "पोटैशियम का स्तर पर्याप्त है।";

      if (
        recommendation.startsWith(
          "Consider soil acidity"
        )
      )
        return "मिट्टी परीक्षण की सलाह के आधार पर मिट्टी की अम्लता का प्रबंधन करने पर विचार करें।";

      if (
        recommendation.startsWith(
          "Consider appropriate alkaline"
        )
      )
        return "उपयुक्त क्षारीय मिट्टी प्रबंधन पर विचार करें।";

      if (
        recommendation.startsWith(
          "Soil pH is within"
        )
      )
        return "मिट्टी का pH उपयुक्त सीमा में है।";

      if (
        recommendation.startsWith(
          "Improve water availability"
        )
      )
        return "फसल की आवश्यकताओं के अनुसार पानी की उपलब्धता में सुधार करें।";

      if (
        recommendation.startsWith(
          "Improve drainage"
        )
      )
        return "जल निकासी में सुधार करें और लंबे समय तक जलभराव से बचें।";

      if (
        recommendation.startsWith(
          "Soil moisture is within"
        )
      )
        return "मिट्टी की नमी उपयुक्त सीमा में है।";

      if (
        recommendation.startsWith(
          "Increase organic matter"
        )
      )
        return "अच्छी तरह प्रबंधित कम्पोस्ट और उपयुक्त फसल अवशेषों का उपयोग करके जैविक पदार्थ बढ़ाएँ।";

      if (
        recommendation.startsWith(
          "Avoid unnecessary additional organic"
        )
      )
        return "अनावश्यक अतिरिक्त जैविक पदार्थ डालने से बचें।";

      if (
        recommendation.startsWith(
          "Organic matter level is adequate"
        )
      )
        return "जैविक पदार्थ का स्तर पर्याप्त है।";
    }

    if (language === "Kannada") {
      if (
        recommendation.startsWith(
          "Nitrogen supplementation"
        )
      )
        return "ನೈಟ್ರೋಜನ್ ಪೂರೈಕೆ ಅಗತ್ಯವಾಗಬಹುದು. ಮಣ್ಣಿನ ಪರೀಕ್ಷೆ ಮತ್ತು ಬೆಳೆ ಅಗತ್ಯಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ಮಾರ್ಗದರ್ಶನವನ್ನು ಅನುಸರಿಸಿ.";

      if (
        recommendation.startsWith(
          "Avoid additional nitrogen"
        )
      )
        return "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆ ಅಥವಾ ಬೆಳೆ ಅಗತ್ಯಗಳ ಆಧಾರದ ಮೇಲೆ ಶಿಫಾರಸು ಮಾಡದಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ನೈಟ್ರೋಜನ್ ತಪ್ಪಿಸಿ.";

      if (
        recommendation.startsWith(
          "Nitrogen level is adequate"
        )
      )
        return "ನೈಟ್ರೋಜನ್ ಮಟ್ಟ ಸಾಕಷ್ಟಿದೆ. ಪ್ರಸ್ತುತ ಮಣ್ಣಿನ ನಿರ್ವಹಣೆಯನ್ನು ಮುಂದುವರಿಸಿ.";

      if (
        recommendation.startsWith(
          "Phosphorus supplementation"
        )
      )
        return "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆ ಮತ್ತು ಬೆಳೆ ಅಗತ್ಯಗಳ ಆಧಾರದ ಮೇಲೆ ಫಾಸ್ಫರಸ್ ಪೂರೈಕೆ ಅಗತ್ಯವಾಗಬಹುದು.";

      if (
        recommendation.startsWith(
          "Avoid additional phosphorus"
        )
      )
        return "ಶಿಫಾರಸು ಮಾಡದಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ಫಾಸ್ಫರಸ್ ತಪ್ಪಿಸಿ.";

      if (
        recommendation.startsWith(
          "Phosphorus level is adequate"
        )
      )
        return "ಫಾಸ್ಫರಸ್ ಮಟ್ಟ ಸಾಕಷ್ಟಿದೆ.";

      if (
        recommendation.startsWith(
          "Potassium supplementation"
        )
      )
        return "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಆಧಾರದ ಮೇಲೆ ಪೊಟ್ಯಾಸಿಯಮ್ ಪೂರೈಕೆ ಅಗತ್ಯವಾಗಬಹುದು.";

      if (
        recommendation.startsWith(
          "Avoid additional potassium"
        )
      )
        return "ಶಿಫಾರಸು ಮಾಡದಿದ್ದರೆ ಹೆಚ್ಚುವರಿ ಪೊಟ್ಯಾಸಿಯಮ್ ತಪ್ಪಿಸಿ.";

      if (
        recommendation.startsWith(
          "Potassium level is adequate"
        )
      )
        return "ಪೊಟ್ಯಾಸಿಯಮ್ ಮಟ್ಟ ಸಾಕಷ್ಟಿದೆ.";

      if (
        recommendation.startsWith(
          "Consider soil acidity"
        )
      )
        return "ಮಣ್ಣಿನ ಪರೀಕ್ಷೆಯ ಶಿಫಾರಸುಗಳ ಆಧಾರದ ಮೇಲೆ ಮಣ್ಣಿನ ಆಮ್ಲೀಯತೆಯ ನಿರ್ವಹಣೆಯನ್ನು ಪರಿಗಣಿಸಿ.";

      if (
        recommendation.startsWith(
          "Consider appropriate alkaline"
        )
      )
        return "ಸೂಕ್ತ ಕ್ಷಾರೀಯ ಮಣ್ಣಿನ ನಿರ್ವಹಣೆಯನ್ನು ಪರಿಗಣಿಸಿ.";

      if (
        recommendation.startsWith(
          "Soil pH is within"
        )
      )
        return "ಮಣ್ಣಿನ pH ಸೂಕ್ತ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆ.";

      if (
        recommendation.startsWith(
          "Improve water availability"
        )
      )
        return "ಬೆಳೆಯ ಅಗತ್ಯಗಳಿಗೆ ಅನುಗುಣವಾಗಿ ನೀರಿನ ಲಭ್ಯತೆಯನ್ನು ಸುಧಾರಿಸಿ.";

      if (
        recommendation.startsWith(
          "Improve drainage"
        )
      )
        return "ಚರಂಡಿ ವ್ಯವಸ್ಥೆಯನ್ನು ಸುಧಾರಿಸಿ ಮತ್ತು ದೀರ್ಘಕಾಲದ ನೀರು ನಿಲ್ಲುವುದನ್ನು ತಪ್ಪಿಸಿ.";

      if (
        recommendation.startsWith(
          "Soil moisture is within"
        )
      )
        return "ಮಣ್ಣಿನ ತೇವಾಂಶವು ಸೂಕ್ತ ವ್ಯಾಪ್ತಿಯಲ್ಲಿದೆ.";

      if (
        recommendation.startsWith(
          "Increase organic matter"
        )
      )
        return "ಸರಿಯಾಗಿ ನಿರ್ವಹಿಸಿದ ಕಾಂಪೋಸ್ಟ್ ಮತ್ತು ಸೂಕ್ತ ಬೆಳೆ ಅವಶೇಷಗಳನ್ನು ಬಳಸಿ ಸಾವಯವ ಪದಾರ್ಥವನ್ನು ಹೆಚ್ಚಿಸಿ.";

      if (
        recommendation.startsWith(
          "Avoid unnecessary additional organic"
        )
      )
        return "ಅಗತ್ಯವಿಲ್ಲದ ಹೆಚ್ಚುವರಿ ಸಾವಯವ ಪದಾರ್ಥವನ್ನು ಸೇರಿಸುವುದನ್ನು ತಪ್ಪಿಸಿ.";

      if (
        recommendation.startsWith(
          "Organic matter level is adequate"
        )
      )
        return "ಸಾವಯವ ಪದಾರ್ಥದ ಮಟ್ಟ ಸಾಕಷ್ಟಿದೆ.";
    }

    return recommendation;
  };

  const translateCropName = (crop: string) => {
    const name = crop.split(" — ")[0];

    const translations: Record<string, Record<string, string>> = {
      Rice: {
        Hindi: "चावल",
        Kannada: "ಅಕ್ಕಿ",
      },
      Wheat: {
        Hindi: "गेहूँ",
        Kannada: "ಗೋಧಿ",
      },
      Maize: {
        Hindi: "मक्का",
        Kannada: "ಮೆಕ್ಕೆಜೋಳ",
      },
      Cotton: {
        Hindi: "कपास",
        Kannada: "ಹತ್ತಿ",
      },
      Groundnut: {
        Hindi: "मूंगफली",
        Kannada: "ಕಡಲೆಕಾಯಿ",
      },
      Chickpea: {
        Hindi: "चना",
        Kannada: "ಕಡಲೆ",
      },
      Pigeonpea: {
        Hindi: "अरहर",
        Kannada: "ತೊಗರಿ",
      },
      Sorghum: {
        Hindi: "ज्वार",
        Kannada: "ಜೋಳ",
      },
      Millet: {
        Hindi: "बाजरा",
        Kannada: "ಸಜ್ಜೆ",
      },
      Sugarcane: {
        Hindi: "गन्ना",
        Kannada: "ಕಬ್ಬು",
      },
    };

    if (language === "English") {
      return crop;
    }

    const translatedName =
      translations[name]?.[language] || name;

    const score = crop.includes(" — ")
      ? crop.split(" — ")[1]
      : "";

    return score
      ? `${translatedName} — ${score}`
      : translatedName;
  };

  const analyzeSoil = async () => {
    setAnalysisError("");

    if (!validateForm()) {
      setResults(null);
      return;
    }

    setIsAnalyzing(true);

    try {
      if (!imageFile) {
    setAnalysisError("Please upload a soil image for CNN analysis.");
    setIsAnalyzing(false);
    return;
  }

  const imageFormData = new FormData();
  imageFormData.append("file", imageFile);

  const cnnResponse = await fetch(
    "http://localhost:8000/predict",
    {
      method: "POST",
      body: imageFormData,
    }
  );

  if (!cnnResponse.ok) {
    throw new Error("CNN analysis failed.");
  }

  const cnnData = await cnnResponse.json();

  console.log("CNN Result:", cnnData);
      const n = Number(formData.nitrogen);
      const p = Number(formData.phosphorus);
      const k = Number(formData.potassium);
      const ph = Number(formData.ph);
      const moisture = Number(formData.moisture);
      const organicMatter = Number(formData.organicMatter);

      // M3 Recommendation Engine conditions
      const conditions = {
        nitrogen:
          n < 20
            ? "Low"
            : n > 50
            ? "High"
            : "Adequate",

        phosphorus:
          p < 10
            ? "Low"
            : p > 40
            ? "High"
            : "Adequate",

        potassium:
          k < 100
            ? "Low"
            : k > 300
            ? "High"
            : "Adequate",

        ph:
          ph < 6
            ? "Acidic"
            : ph > 7.5
            ? "Alkaline"
            : "Suitable",

        moisture:
          moisture < 30
            ? "Low"
            : moisture > 70
            ? "High"
            : "Suitable",

        organicMatter:
          organicMatter < 2
            ? "Low"
            : organicMatter > 5
            ? "High"
            : "Adequate",
      };

      // M3 Soil Health scoring
      const parameterScore = (
        value: number,
        minimum: number,
        maximum: number
      ) => {
        if (value >= minimum && value <= maximum) {
          return 100;
        }

        const distance =
          value < minimum
            ? minimum - value
            : value - maximum;

        const range = maximum - minimum;

        return Math.max(
          0,
          100 - (distance / range) * 100
        );
      };

      const healthScores = [
        parameterScore(n, 20, 50),
        parameterScore(p, 10, 40),
        parameterScore(k, 100, 300),
        parameterScore(ph, 6, 7.5),
        parameterScore(moisture, 30, 70),
        parameterScore(organicMatter, 2, 5),
      ];

      const healthScore = Number(
        (
          healthScores.reduce(
            (total, score) => total + score,
            0
          ) / healthScores.length
        ).toFixed(2)
      );

      const healthStatus =
        healthScore >= 80
          ? "Healthy"
          : healthScore >= 60
          ? "Moderately Healthy"
          : healthScore >= 40
          ? "Needs Improvement"
          : "Poor";

      // M3 recommendation rules
      const recommendations: string[] = [];

      if (n < 20) {
        recommendations.push(
          "Nitrogen supplementation may be required. Follow soil-test and crop-specific guidance."
        );
      } else if (n > 50) {
        recommendations.push(
          "Avoid additional nitrogen unless recommended by soil testing or crop requirements."
        );
      } else {
        recommendations.push(
          "Nitrogen level is adequate. Maintain current soil management."
        );
      }

      if (p < 10) {
        recommendations.push(
          "Phosphorus supplementation may be required based on soil-test and crop requirements."
        );
      } else if (p > 40) {
        recommendations.push(
          "Avoid additional phosphorus unless recommended."
        );
      } else {
        recommendations.push(
          "Phosphorus level is adequate."
        );
      }

      if (k < 100) {
        recommendations.push(
          "Potassium supplementation may be required based on soil testing."
        );
      } else if (k > 300) {
        recommendations.push(
          "Avoid additional potassium unless recommended."
        );
      } else {
        recommendations.push(
          "Potassium level is adequate."
        );
      }

      if (ph < 6) {
        recommendations.push(
          "Consider soil acidity management based on soil-test recommendations."
        );
      } else if (ph > 7.5) {
        recommendations.push(
          "Consider appropriate alkaline-soil management."
        );
      } else {
        recommendations.push(
          "Soil pH is within the suitable range."
        );
      }

      if (moisture < 30) {
        recommendations.push(
          "Improve water availability according to crop requirements."
        );
      } else if (moisture > 70) {
        recommendations.push(
          "Improve drainage and avoid prolonged waterlogging."
        );
      } else {
        recommendations.push(
          "Soil moisture is within the suitable range."
        );
      }

      if (organicMatter < 2) {
        recommendations.push(
          "Increase organic matter using well-managed compost and suitable crop residues."
        );
      } else if (organicMatter > 5) {
        recommendations.push(
          "Avoid unnecessary additional organic amendments."
        );
      } else {
        recommendations.push(
          "Organic matter level is adequate."
        );
      }

      // Prototype crop suitability
      const cropRanges = [
        {
          name: "Rice",
          n: [20, 60],
          p: [10, 40],
          k: [100, 250],
          ph: [5.5, 7.5],
          moisture: [50, 80],
          om: [1.5, 4],
        },
        {
          name: "Wheat",
          n: [25, 60],
          p: [12, 40],
          k: [100, 250],
          ph: [6, 7.5],
          moisture: [35, 65],
          om: [1.5, 4],
        },
        {
          name: "Maize",
          n: [25, 60],
          p: [12, 40],
          k: [100, 300],
          ph: [5.5, 7.5],
          moisture: [40, 70],
          om: [1.5, 4],
        },
        {
          name: "Cotton",
          n: [20, 60],
          p: [10, 40],
          k: [100, 300],
          ph: [5.5, 8],
          moisture: [35, 65],
          om: [1.5, 4],
        },
        {
          name: "Groundnut",
          n: [20, 50],
          p: [10, 35],
          k: [80, 250],
          ph: [5.5, 7],
          moisture: [35, 65],
          om: [1, 3.5],
        },
        {
          name: "Chickpea",
          n: [20, 50],
          p: [10, 35],
          k: [80, 250],
          ph: [6, 8],
          moisture: [25, 55],
          om: [1, 3.5],
        },
        {
          name: "Pigeonpea",
          n: [20, 50],
          p: [10, 35],
          k: [80, 250],
          ph: [6, 7.5],
          moisture: [30, 60],
          om: [1, 3.5],
        },
        {
          name: "Sorghum",
          n: [20, 55],
          p: [10, 35],
          k: [80, 250],
          ph: [5.5, 8],
          moisture: [25, 60],
          om: [1, 3.5],
        },
        {
          name: "Millet",
          n: [15, 45],
          p: [8, 30],
          k: [60, 200],
          ph: [5.5, 7.5],
          moisture: [20, 55],
          om: [0.8, 3],
        },
        {
          name: "Sugarcane",
          n: [30, 70],
          p: [15, 45],
          k: [120, 350],
          ph: [6, 7.5],
          moisture: [50, 80],
          om: [2, 5],
        },
      ];

      const cropScore = (
        value: number,
        range: number[]
      ) => {
        const [min, max] = range;

        if (value >= min && value <= max) {
          return 100;
        }

        const distance =
          value < min
            ? min - value
            : value - max;

        return Math.max(
          0,
          100 - (distance / (max - min)) * 100
        );
      };

      const cropResults = cropRanges
        .map((crop) => {
          const score =
            (
              cropScore(n, crop.n) +
              cropScore(p, crop.p) +
              cropScore(k, crop.k) +
              cropScore(ph, crop.ph) +
              cropScore(moisture, crop.moisture) +
              cropScore(organicMatter, crop.om)
            ) / 6;

          return {
            name: crop.name,
            score,
          };
        })
        .sort((a, b) => b.score - a.score);

      const newResult: Results = {
        healthScore,
        healthStatus,

        soilValues: {
          nitrogen: n,
          phosphorus: p,
          potassium: k,
          ph,
          moisture,
          organicMatter,
        },

        conditions,

        crops: cropResults
          .slice(0, 5)
          .map(
            (crop) =>
              `${crop.name} — ${crop.score.toFixed(2)}%`
          ),

        recommendations,
        soilType: cnnData.soil_type,
        soilConfidence: cnnData.confidence,
      };

      setResults(newResult);

      const updatedHistory = [
        newResult,
        ...history,
      ];

      setHistory(updatedHistory);

      localStorage.setItem(
        "soilAnalysisHistory",
        JSON.stringify(updatedHistory)
      );

      setIsAnalyzing(false);
    } catch (error) {
      console.error(error);

      setAnalysisError(
        "Something went wrong while analyzing the soil. Please try again."
      );

      setResults(null);
      setIsAnalyzing(false);
    }
  };

  const conditionLabels: Record<
    string,
    string
  > = {
    nitrogen: t.nitrogen,
    phosphorus: t.phosphorus,
    potassium: t.potassium,
    ph: "pH",
    moisture: t.moisture,
    organicMatter: t.organicMatter,
  };

  return (
    <main className="min-h-screen bg-green-50 px-4 py-6">
      <div className="mx-auto w-full max-w-2xl">

        {/* Header */}
        <div className="mb-6 flex items-center justify-between">
          <div>
            <h1 className="text-3xl font-bold text-green-800">
              Soil Smart 🌱
            </h1>

            <p className="text-sm text-gray-600">
              {t.title}
            </p>
          </div>

          <select
            value={language}
            onChange={(e) =>
              setLanguage(e.target.value)
            }
            className="rounded-lg border bg-white px-2 py-2 text-sm"
          >
            <option>English</option>
            <option>Hindi</option>
            <option>Kannada</option>
          </select>
        </div>

        {/* Welcome */}
        <section className="mb-5 rounded-2xl bg-white p-5 shadow">
          <h2 className="mb-2 text-xl font-semibold text-gray-800">
            {t.welcome}
          </h2>

          <p className="text-sm text-gray-600">
            {t.welcomeText}
          </p>
        </section>

        {/* Image Upload */}
        <section className="mb-5 rounded-2xl bg-white p-5 shadow">
          <h2 className="mb-3 text-lg font-semibold text-gray-800">
            {t.soilImage}
          </h2>

          <input
            type="file"
            accept="image/jpeg,image/png"
            capture="environment"
            onChange={handleImageChange}
            className="w-full rounded-lg border p-3 text-sm"
          />

          {imageError && (
            <p className="mt-2 text-sm text-red-600">
              {imageError}
            </p>
          )}

          {imagePreview && (
            <div className="mt-4">
              <img
                src={imagePreview}
                alt="Soil preview"
                className="h-56 w-full rounded-2xl border-2 border-green-100 object-cover shadow-sm"
              />

              <button
                type="button"
                onClick={() => {
                  setImagePreview(null);
                  setImageFile(null);
                  setImageError("");
                }}
                className="mt-2 w-full rounded-lg bg-gray-100 py-2 text-sm"
              >
                {t.removeImage}
              </button>
            </div>
          )}
        </section>

        {/* Soil Inputs */}
        <section className="mb-5 rounded-2xl bg-white p-5 shadow">
          <h2 className="mb-4 text-xl font-bold text-gray-800">
            {t.soilParameters}
          </h2>

          {[
            [
              "nitrogen",
              language === "Hindi"
                ? "नाइट्रोजन (N)"
                : language === "Kannada"
                ? "ನೈಟ್ರೋಜನ್ (N)"
                : "Nitrogen (N)",
            ],

            [
              "phosphorus",
              language === "Hindi"
                ? "फॉस्फोरस (P)"
                : language === "Kannada"
                ? "ಫಾಸ್ಫರಸ್ (P)"
                : "Phosphorus (P)",
            ],

            [
              "potassium",
              language === "Hindi"
                ? "पोटैशियम (K)"
                : language === "Kannada"
                ? "ಪೊಟ್ಯಾಸಿಯಮ್ (K)"
                : "Potassium (K)",
            ],

            ["ph", "pH"],

            [
              "moisture",
              language === "Hindi"
                ? "नमी (%)"
                : language === "Kannada"
                ? "ತೇವಾಂಶ (%)"
                : "Moisture (%)",
            ],

            [
              "organicMatter",
              language === "Hindi"
                ? "जैविक पदार्थ (%)"
                : language === "Kannada"
                ? "ಸಾವಯವ ಪದಾರ್ಥ (%)"
                : "Organic Matter (%)",
            ],
          ].map(([name, label]) => (
            <div
              key={name}
              className="mb-4"
            >
              <label className="mb-1 block text-sm font-medium text-gray-700">
                {label}
              </label>

              <input
  type="number"
  step="any"
  name={name}
  value={
    formData[
      name as keyof SoilData
    ]
  }
  onChange={handleInputChange}
  placeholder={
    name === "nitrogen"
      ? "e.g. 40"
      : name === "phosphorus"
      ? "e.g. 25"
      : name === "potassium"
      ? "e.g. 200"
      : name === "ph"
      ? "e.g. 6.8"
      : name === "moisture"
      ? "e.g. 50"
      : "e.g. 3"
  }
  className="w-full rounded-lg border px-3 py-3 outline-none focus:ring-2 focus:ring-green-500"
/>
              {formErrors[name] && (
                <p className="mt-1 text-xs text-red-600">
                  {formErrors[name]}
                </p>
              )}
            </div>
          ))}

          {analysisError && (
            <p className="mb-3 rounded-lg bg-red-50 p-3 text-sm text-red-600">
              {analysisError}
            </p>
          )}

          <button
            onClick={analyzeSoil}
            disabled={isAnalyzing}
            className="w-full rounded-xl bg-green-700 py-3 font-semibold text-white hover:bg-green-800 disabled:cursor-not-allowed disabled:opacity-60"
          >
            {isAnalyzing
              ? t.analyzing
              : t.analyze}
          </button>
          <button
  type="button"
  onClick={() => {
    setFormData({
      nitrogen: "",
      phosphorus: "",
      potassium: "",
      ph: "",
      moisture: "",
      organicMatter: "",
    });

    setFormErrors({});

setResults(null);

setAnalysisError("");

setImagePreview(null);

setImageFile(null);

setImageError("");
  }}
  disabled={isAnalyzing}
  className="mt-3 w-full rounded-xl border border-green-700 bg-white py-3 font-semibold text-green-700 hover:bg-green-50 disabled:cursor-not-allowed disabled:opacity-60"
>
  🔄 {t.newAnalysis}
</button>
        </section>

        {/* Results */}
        {results && (
          <section className="space-y-5">
            {/* CNN Soil Classification */}
<div className="rounded-2xl bg-white p-5 shadow">
  <h2 className="mb-4 text-xl font-bold text-green-800">
    🤖 AI Soil Image Classification
  </h2>

  <div className="rounded-xl bg-green-50 p-4">
    <div className="flex items-center justify-between">
      <span className="font-medium text-gray-700">
        Detected Soil Type
      </span>

      <span className="rounded-full bg-green-700 px-4 py-2 font-bold text-white">
        {results.soilType}
      </span>
    </div>

    <div className="mt-4 flex items-center justify-between">
      <span className="font-medium text-gray-700">
        CNN Confidence
      </span>

      <span className="font-bold text-green-700">
        {typeof results.soilConfidence === "number"
        ? results.soilConfidence.toFixed(2)
        : "N/A"}%
      </span>
    </div>

    <div className="mt-3 h-3 w-full overflow-hidden rounded-full bg-gray-200">
      <div
        className="h-full rounded-full bg-green-600 transition-all duration-500"
        style={{
          width: `${Math.min(
            typeof results.soilConfidence === "number"
            ?results.soilConfidence
            : 0,
            100
            )}%`,
        }}
      />
    </div>
  </div>
</div>
            {/* Health */}
            <div className="rounded-2xl bg-white p-5 shadow">
              <h2 className="mb-3 text-xl font-bold text-green-800">
                {t.soilHealth}
              </h2>

              <div className="text-center">
                <p className="text-5xl font-bold text-green-700">
                  {results.healthScore}
                </p>

                <p className="text-sm text-gray-500">
                  / 100
                </p>

                <p className="mt-2 text-lg font-semibold">
                  {translateHealthStatus(
                    results.healthStatus
                  )}
                </p>
                <div className="mt-4 h-3 w-full overflow-hidden rounded-full bg-gray-200">
  <div
    className="h-full rounded-full bg-green-600 transition-all duration-500"
    style={{
      width: `${results.healthScore}%`,
    }}
  />
</div>
              </div>
            </div>

            {/* Conditions */}
            <div className="rounded-2xl bg-white p-5 shadow">
              <h2 className="mb-4 text-xl font-bold text-gray-800">
                {t.conditions}
              </h2>

              <div className="space-y-3">
                {Object.entries(
                  results.conditions
                ).map(
                  ([parameter, condition]) => (
                    <div
                      key={parameter}
                      className="flex justify-between rounded-lg bg-gray-50 p-3"
                    >
                      <span className="font-medium">
                        {conditionLabels[
                          parameter
                        ] || parameter}
                      </span>

                      <span
  className={`rounded-full px-3 py-1 text-sm font-semibold ${
    condition === "Low"
      ? "bg-red-100 text-red-700"
      : condition === "High"
      ? "bg-orange-100 text-orange-700"
      : condition === "Acidic"
      ? "bg-yellow-100 text-yellow-700"
      : condition === "Alkaline"
      ? "bg-purple-100 text-purple-700"
      : "bg-green-100 text-green-700"
  }`}
>
  {translateCondition(condition)}
</span>
                    </div>
                  )
                )}
              </div>
            </div>

            {/* Parameters */}
            <div className="rounded-2xl bg-white p-5 shadow">
              <h2 className="mb-4 text-xl font-bold text-gray-800">
                {t.soilParameters}
              </h2>

              <div className="grid grid-cols-2 gap-3">
                {[
                  [
                    "N",
                    formData.nitrogen,
                  ],
                  [
                    "P",
                    formData.phosphorus,
                  ],
                  [
                    "K",
                    formData.potassium,
                  ],
                  [
                    "pH",
                    formData.ph,
                  ],
                  [
                    t.moisture,
                    formData.moisture,
                  ],
                  [
                    t.organicMatter,
                    formData.organicMatter,
                  ],
                ].map(
                  ([label, value]) => (
                    <div
                      key={label}
                      className="rounded-lg bg-green-50 p-3 text-center"
                    >
                      <p className="text-xs text-gray-500">
                        {label}
                      </p>

                      <p className="text-lg font-bold text-green-800">
                        {value}
                      </p>
                    </div>
                  )
                )}
              </div>
            </div>

            {/* Recommendations */}
            <div className="rounded-2xl bg-white p-5 shadow">
              <h2 className="mb-4 text-xl font-bold text-gray-800">
                {t.recommendations}
              </h2>

              <div className="space-y-3">
                {results.recommendations.map(
                  (
                    recommendation,
                    index
                  ) => (
                    <div
  key={index}
  className="flex items-start gap-3 rounded-xl border border-green-100 bg-green-50 p-4 text-sm text-gray-700"
>
  <span className="mt-0.5 text-lg">💡</span>

  <p className="leading-6">
    {translateRecommendation(recommendation)}
  </p>
</div>
                  )
                )}
              </div>
            </div>

            {/* Crops */}
            <div className="rounded-2xl bg-white p-5 shadow">
              <h2 className="mb-4 text-xl font-bold text-gray-800">
                {t.crops}
              </h2>

              <div className="space-y-3">
                {results.crops.map(
                  (crop, index) => (
                    <div
  key={index}
  className="flex items-center justify-between rounded-xl border border-green-100 bg-green-50 p-4"
>
  <div className="flex items-center gap-3">
    <span className="flex h-8 w-8 items-center justify-center rounded-full bg-green-700 text-sm font-bold text-white">
      {index + 1}
    </span>

    <span className="font-semibold text-green-900">
      {translateCropName(crop).split(" — ")[0]}
    </span>
  </div>

  <span className="text-sm font-bold text-green-700">
    {crop.split(" — ")[1]}
  </span>
</div>
                  )
                )}
              </div>
            </div>

          </section>
        )}

        {/* History */}
  {history.length > 0 && (
  <section className="mt-5 rounded-2xl bg-white p-5 shadow">
    <div className="mb-4 flex items-center justify-between">
      <h2 className="text-xl font-bold text-green-800">
        {t.history}
      </h2>

      <button
        onClick={() => {
          setHistory([]);
          localStorage.removeItem("soilAnalysisHistory");
        }}
        className="rounded-lg bg-red-100 px-3 py-2 text-sm font-semibold text-red-700 hover:bg-red-200"
      >
        {language === "Hindi"
          ? "इतिहास साफ़ करें"
          : language === "Kannada"
          ? "ಇತಿಹಾಸವನ್ನು ತೆರವುಗೊಳಿಸಿ"
          : "Clear History"}
      </button>
    </div>

    <div className="space-y-3">
      {(showAllHistory ? history : history.slice(0, 3)).map(
        (item, index) => (
          <div
            key={index}
            className="rounded-xl border border-green-100 bg-green-50 p-4"
          >
            <p className="font-semibold text-green-800">
              {item.healthScore}/100 —{" "}
              {translateHealthStatus(item.healthStatus)}
            </p>

            <p className="mt-1 text-sm text-gray-700">
              N:{" "}
              {translateCondition(item.conditions.nitrogen)} | P:{" "}
              {translateCondition(item.conditions.phosphorus)} | K:{" "}
              {translateCondition(item.conditions.potassium)}
            </p>

            <p className="mt-1 text-sm text-gray-700">
              {item.soilValues
                ? language === "Hindi"
                  ? `pH: ${item.soilValues.ph} | नमी: ${item.soilValues.moisture} | जैविक पदार्थ: ${item.soilValues.organicMatter}`
                  : language === "Kannada"
                  ? `pH: ${item.soilValues.ph} | ತೇವಾಂಶ: ${item.soilValues.moisture} | ಸಾವಯವ ಪದಾರ್ಥ: ${item.soilValues.organicMatter}`
                  : `pH: ${item.soilValues.ph} | Moisture: ${item.soilValues.moisture} | Organic Matter: ${item.soilValues.organicMatter}`
                : t.olderAnalysis}
            </p>

            {item.soilType && (
              <p className="mt-2 text-sm text-gray-700">
                <span className="font-semibold">
                  🤖{" "}
                  {language === "Hindi"
                    ? "AI मिट्टी का प्रकार:"
                    : language === "Kannada"
                    ? "AI ಮಣ್ಣಿನ ಪ್ರಕಾರ:"
                    : "AI Soil Type:"}
                </span>{" "}
                {translateSoilType(item.soilType)}
              </p>
            )}

            {typeof item.soilConfidence === "number" && (
              <p className="mt-1 text-sm text-gray-700">
                <span className="font-semibold">
                  {language === "Hindi"
                    ? "CNN विश्वसनीयता:"
                    : language === "Kannada"
                    ? "CNN ವಿಶ್ವಾಸಾರ್ಹತೆ:"
                    : "CNN Confidence:"}
                </span>{" "}
                {item.soilConfidence.toFixed(2)}%
              </p>
            )}
          </div>
        )
      )}
    </div>

    {history.length > 3 && (
      <button
        onClick={() => setShowAllHistory(!showAllHistory)}
        className="mt-4 w-full rounded-lg bg-green-100 px-4 py-2 font-semibold text-green-800 hover:bg-green-200"
      >
        {showAllHistory
          ? language === "Hindi"
            ? "कम दिखाएँ"
            : language === "Kannada"
            ? "ಕಡಿಮೆ ತೋರಿಸಿ"
            : "Show Less"
          : language === "Hindi"
          ? `और ${history.length - 3} विश्लेषण दिखाएँ`
          : language === "Kannada"
          ? `ಇನ್ನೂ ${history.length - 3} ವಿಶ್ಲೇಷಣೆಗಳನ್ನು ತೋರಿಸಿ`
          : `Show ${history.length - 3} More Analyses`}
      </button>
    )}
  </section>
)}


        {/* Footer */}
        <footer className="mt-8 pb-4 text-center text-xs text-gray-500">
          {t.footer}
        </footer>

      </div>
    </main>
  );
}

