<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Arquitectura de Anillos MIF-NEXUS v2.0</title>
<style>
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    body {
        background: linear-gradient(135deg, #1a2a6c, #b21f1f, #fdbb2d);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        padding: 40px;
        min-height: 100vh;
        color: #333;
    }

    .header {
        color: white;
        margin-bottom: 30px;
    }

    h1 {
        font-size: 2.5rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        margin-bottom: 10px;
    }

    .subtitle {
        font-size: 1.2rem;
        opacity: 0.9;
    }

    .version-badge {
        background: #27ae60;
        color: white;
        padding: 5px 15px;
        border-radius: 20px;
        font-size: 0.9rem;
        margin-top: 10px;
        display: inline-block;
    }

    .canvas {
        width: 1200px;
        height: 1200px;
        margin: 40px auto;
        position: relative;
        background: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        backdrop-filter: blur(10px);
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
    }

    /* ===== ANILLOS (POR DEBAJO) ===== */
    .ring {
        position: absolute;
        border-radius: 50%;
        border: 4px solid rgba(255,255,255,0.7);
        backdrop-filter: blur(4px);
        transition: all 0.5s ease;
        animation: pulse-ring 8s infinite ease-in-out;
        z-index: 1;
    }

    @keyframes pulse-ring {
        0%, 100% { transform: scale(1); opacity: 0.8; }
        50% { transform: scale(1.05); opacity: 1; }
    }

    /* Anillo de Dominios */
    .ring-0 { 
        width: 200px; 
        height: 200px; 
        top: 500px; 
        left: 500px; 
        background: rgba(231, 76, 60, 0.15); 
        animation-delay: 0s;
        border-color: rgba(231, 76, 60, 0.8);
    }
    
    .ring-1 { 
        width: 300px; 
        height: 300px; 
        top: 450px; 
        left: 450px; 
        background: rgba(52,152,219,0.12); 
        animation-delay: 0.5s;
    }
    
    .ring-2 { 
        width: 500px; 
        height: 500px; 
        top: 350px; 
        left: 350px; 
        background: rgba(46,204,113,0.12); 
        animation-delay: 1s;
    }
    
    .ring-3 { 
        width: 700px; 
        height: 700px; 
        top: 250px; 
        left: 250px; 
        background: rgba(155,89,182,0.12); 
        animation-delay: 1.5s;
    }
    
    .ring-4 { 
        width: 900px; 
        height: 900px; 
        top: 150px; 
        left: 150px; 
        background: rgba(241,196,15,0.12); 
        animation-delay: 2s;
    }

    /* ===== ETIQUETAS ===== */
    .ring-label {
        position: absolute;
        font-size: 1.4rem;
        font-weight: bold;
        background: rgba(255,255,255,0.85);
        padding: 8px 16px;
        border-radius: 10px;
        z-index: 10;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease;
    }

    .ring-label:hover {
        transform: scale(1.1);
        box-shadow: 0 6px 12px rgba(0,0,0,0.15);
    }

    .label-0 { top: 620px; left: 550px; color: #e74c3c; }
    .label-1 { top: 780px; left: 550px; color: #3498db; }
    .label-2 { top: 310px; left: 560px; color: #2ecc71; }
    .label-3 { top: 200px; left: 570px; color: #9b59b6; }
    .label-4 { top: 100px; left: 580px; color: #f1c40f; }

    /* ===== COMPONENTES (POR ENCIMA) ===== */
    .component {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        position: absolute;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 0.75rem;
        font-weight: bold;
        text-align: center;
        padding: 5px;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 8px rgba(0,0,0,.3);
        animation: float 6s infinite ease-in-out;
        cursor: pointer;
        z-index: 5;
    }

    @keyframes float {
        0%, 100% { transform: translateY(0) rotate(0deg); }
        25% { transform: translateY(-8px) rotate(2deg); }
        50% { transform: translateY(-12px) rotate(0deg); }
        75% { transform: translateY(-8px) rotate(-2deg); }
    }

    /* ==== EFECTO DE SELECCIÓN ==== */
    .component:hover {
        transform: scale(1.18) rotate(5deg);
        background: white !important;
        color: black !important;
        box-shadow: 0 0 18px rgba(0,0,0,0.25),
                    0 0 35px rgba(0,0,0,0.15);
        animation-play-state: paused;
        z-index: 100;
    }

    /* Líneas de conexión animadas */
    .connection-line {
        position: absolute;
        height: 2px;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.7), transparent);
        transform-origin: left center;
        z-index: 2;
        animation: pulse-line 3s infinite ease-in-out;
    }

    @keyframes pulse-line {
        0%, 100% { opacity: 0.3; }
        50% { opacity: 0.8; }
    }

    /* Detalles de anillos */
    .details-section {
        max-width: 1200px;
        margin: 40px auto;
        padding: 30px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    }

    .details-section h2 {
        color: #2c3e50;
        margin-bottom: 30px;
        font-size: 2rem;
    }

    .ring-details {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
        gap: 25px;
        margin-bottom: 40px;
    }

    .detail-card {
        background: white;
        border-radius: 15px;
        padding: 25px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.08);
        transition: all 0.3s ease;
        border-left: 5px solid;
        animation: card-enter 0.6s ease-out;
    }

    @keyframes card-enter {
        0% { transform: translateY(20px); opacity: 0; }
        100% { transform: translateY(0); opacity: 1; }
    }

    .detail-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    }

    .detail-card.ring0 { border-left-color: #e74c3c; }
    .detail-card.ring1 { border-left-color: #3498db; }
    .detail-card.ring2 { border-left-color: #2ecc71; }
    .detail-card.ring3 { border-left-color: #9b59b6; }
    .detail-card.ring4 { border-left-color: #f1c40f; }

    .detail-card h3 {
        margin-bottom: 15px;
        font-size: 1.3rem;
        color: #2c3e50;
    }

    .component-list {
        list-style: none;
        text-align: left;
    }

    .component-list li {
        padding: 8px 0;
        border-bottom: 1px solid #eee;
        font-size: 0.9rem;
        position: relative;
        padding-left: 20px;
        transition: all 0.2s ease;
    }

    .component-list li:hover {
        background: #f8f9fa;
        padding-left: 25px;
    }

    .component-list li:before {
        content: "▸";
        position: absolute;
        left: 0;
        color: #3498db;
    }

    .tech-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
        gap: 10px;
        margin-top: 15px;
    }

    .tech-item {
        background: #f8f9fa;
        padding: 8px;
        border-radius: 5px;
        font-size: 0.8rem;
        text-align: center;
        transition: all 0.2s ease;
    }

    .tech-item:hover {
        background: #e9ecef;
        transform: translateY(-2px);
    }

    .interaction-flow {
        background: linear-gradient(135deg, #2c3e50, #34495e);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-top: 30px;
        font-family: 'Courier New', monospace;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        animation: flow-glow 4s infinite alternate;
    }

    @keyframes flow-glow {
        0% { box-shadow: 0 5px 15px rgba(0,0,0,0.2); }
        100% { box-shadow: 0 5px 20px rgba(52, 152, 219, 0.4); }
    }

    .footer {
        margin-top: 40px;
        color: white;
        font-size: 0.9rem;
        opacity: 0.8;
    }

    /* Nuevos estilos para el dominio económico */
    .economic-flow {
        background: linear-gradient(135deg, #27ae60, #2ecc71);
        color: white;
        padding: 25px;
        border-radius: 15px;
        margin-top: 30px;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
    }

    .capital-grid {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
        gap: 15px;
        margin-top: 20px;
    }

    .capital-item {
        background: rgba(255,255,255,0.1);
        padding: 15px;
        border-radius: 10px;
        text-align: center;
    }

    .capital-item h4 {
        margin-bottom: 10px;
        font-size: 1.1rem;
    }

    /* Responsive */
    @media (max-width: 1300px) {
        .canvas {
            transform: scale(0.8);
        }
    }

    @media (max-width: 1000px) {
        .canvas {
            transform: scale(0.6);
        }
    }

    @media (max-width: 700px) {
        .canvas {
            transform: scale(0.5);
        }
        
        h1 {
            font-size: 1.8rem;
        }
        
        .ring-details {
            grid-template-columns: 1fr;
        }
        
        .capital-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
</head>
<body>

<div class="header">
    <h1>ARQUITECTURA DE ANILLOS MIF-NEXUS v2.0</h1>
    <p class="subtitle">8 Dominios Operativos + 5 Anillos Concéntricos - Con Integración Económica Completa</p>
    <div class="version-badge">NUEVO: Dominio 8 - Economía y Finanzas Sostenibles</div>
</div>

<div class="canvas">
    <!-- Anillos (POR DEBAJO con z-index: 1) -->
    <div class="ring ring-0"></div>
    <div class="ring ring-1"></div>
    <div class="ring ring-2"></div>
    <div class="ring ring-3"></div>
    <div class="ring ring-4"></div>

    <!-- Labels -->
    <div class="ring-label label-0">8 DOMINIOS</div>
    <div class="ring-label label-1">ANILLO 1</div>
    <div class="ring-label label-2">ANILLO 2</div>
    <div class="ring-label label-3">ANILLO 3</div>
    <div class="ring-label label-4">ANILLO 4</div>
</div>

<!-- Detalles de los anillos -->
<div class="details-section">
    <h2>ESPECIFICACIÓN COMPLETA CON DOMINIO ECONÓMICO INTEGRADO</h2>
    
    <div class="ring-details">
        <!-- 8 DOMINIOS -->
        <div class="detail-card ring0">
            <h3>🎯 8 DOMINIOS OPERATIVOS</h3>
            <p><strong>Propósito:</strong> Base operacional especializada para ejecución técnica y económica</p>
            
            <h4>Dominios Principales:</h4>
            <ul class="component-list">
                <li><strong>D1:</strong> Recursos y Materia Prima</li>
                <li><strong>D2:</strong> Infraestructura y Activos</li>
                <li><strong>D3:</strong> Datos, Monitoreo y Control</li>
                <li><strong>D4:</strong> Estrategia, Gestión y Gobernanza</li>
                <li><strong>D5:</strong> Seguridad, Riesgo y Resiliencia</li>
                <li><strong>D6:</strong> Operaciones y Eficiencia Energética</li>
                <li><strong>D7:</strong> Transición Energética Integrada</li>
                <li><strong>💎 D8:</strong> <strong>Economía y Finanzas Sostenibles</strong></li>
            </ul>
        </div>

        <!-- DOMINIO 8 ESPECÍFICO -->
        <div class="detail-card ring0">
            <h3>💎 D8: ECONOMÍA Y FINANZAS SOSTENIBLES</h3>
            <p><strong>Propósito:</strong> Garantizar rentabilidad integral y flujos económicos regenerativos</p>
            
            <h4>Componentes Principales:</h4>
            <ul class="component-list">
                <li><strong>Modelos de Negocio Circulares</strong></li>
                <li><strong>Flujos de Caja Multi-capital</strong></li>
                <li><strong>ROI Sostenible (S-ROI)</strong></li>
                <li><strong>Presupuestos Regenerativos</strong></li>
                <li><strong>Análisis Costo-Beneficio Integral</strong></li>
                <li><strong>Inversión de Impacto</strong></li>
                <li><strong>Monetización de Externalidades</strong></li>
            </ul>
            
            <h4>Métricas Clave:</h4>
            <div class="tech-grid">
                <div class="tech-item">S-ROI ≥ 15%</div>
                <div class="tech-item">TIR Verde</div>
                <div class="tech-item">Valor por Externalidad</div>
                <div class="tech-item">Costo Ciclo de Vida</div>
            </div>
        </div>

        <!-- ANILLO 1 -->
        <div class="detail-card ring1">
            <h3>🎯 ANILLO 1: NÚCLEO TÉCNICO-ECONÓMICO</h3>
            <p><strong>Propósito:</strong> Ejecución operacional con optimización económica en tiempo real</p>
            
            <h4>Componentes Principales:</h4>
            <ul class="component-list">
                <li><strong>8 Dominios Operativos</strong> (D1-D8)</li>
                <li><strong>Gestión Técnica y Económica Integrada</strong></li>
                <li><strong>Procesos Core con KPIs Financieros</strong></li>
                <li><strong>Optimización Costo-Beneficio</strong></li>
                <li><strong>Ejecución en Tiempo Real</strong></li>
            </ul>
            
            <h4>Integración Económica:</h4>
            <div class="tech-grid">
                <div class="tech-item">Costos Operativos</div>
                <div class="tech-item">Eficiencia por Recurso</div>
                <div class="tech-item">ROI por Activo</div>
                <div class="tech-item">Presupuestos Dinámicos</div>
            </div>
        </div>

        <!-- ANILLO 2 -->
        <div class="detail-card ring2">
            <h3>🌐 ANILLO 2: PLATAFORMA DIGITAL Y FINANCIERA</h3>
            <p><strong>Propósito:</strong> Sistema nervioso digital con inteligencia económica integrada</p>
            
            <h4>Componentes Principales:</h4>
            <ul class="component-list">
                <li><strong>Dashboard Nexus Interactivo</strong></li>
                <li><strong>API de Integración Abierta</strong></li>
                <li><strong>Base de Datos Unificada</strong></li>
                <li><strong>Motor de IA y Analítica Económica</strong></li>
                <li><strong>Gemelos Digitales con Simulación Económica</strong></li>
            </ul>
            
            <h4>Tecnologías Integradas:</h4>
            <div class="tech-grid">
                <div class="tech-item">React.js + D3.js</div>
                <div class="tech-item">Python + TensorFlow</div>
                <div class="tech-item">PostgreSQL + TimescaleDB</div>
                <div class="tech-item">Blockchain Finance</div>
            </div>
        </div>
    </div>

    <div class="ring-details">
        <!-- ANILLO 3 -->
        <div class="detail-card ring3">
            <h3>🌱 ANILLO 3: SOSTENIBILIDAD Y ECONOMÍA REGENERATIVA</h3>
            <p><strong>Propósito:</strong> Garantizar impacto neto positivo con rentabilidad verificada</p>
            
            <h4>Componentes Principales:</h4>
            <ul class="component-list">
                <li><strong>Carbono Negativo Verificado</strong></li>
                <li><strong>Agua Neto Positivo</strong></li>
                <li><strong>Biodiversidad +30%</strong></li>
                <li><strong>Economía Circular 95%</strong></li>
                <li><strong>Certificaciones Automáticas</strong></li>
                <li><strong>Bonos Verdes y Mercados de Carbono</strong></li>
            </ul>
            
            <h4>Valor Económico Generado:</h4>
            <div class="tech-grid">
                <div class="tech-item">Primas por Certificación</div>
                <div class="tech-item">Ahorros por Eficiencia</div>
                <div class="tech-item">Ingresos por Carbono</div>
                <div class="tech-item">Valor de Marca +</div>
            </div>
        </div>

        <!-- ANILLO 4 -->
        <div class="detail-card ring4">
            <h3>🤝 ANILLO 4: ECOSISTEMA NEXUS Y MERCADOS</h3>
            <p><strong>Propósito:</strong> Gobernanza expandida, innovación abierta y mercados globales</p>
            
            <h4>Componentes Principales:</h4>
            <ul class="component-list">
                <li><strong>Comité Nexus Multi-stakeholder</strong></li>
                <li><strong>Innovación Abierta</strong></li>
                <li><strong>Comunidad de Desarrollo</strong></li>
                <li><strong>Mercado de Carbono y ESG</strong></li>
                <li><strong>Educación Continua</strong></li>
                <li><strong>Fondos de Inversión de Impacto</strong></li>
            </ul>
            
            <h4>Plataformas de Ecosistema:</h4>
            <div class="tech-grid">
                <div class="tech-item">Nexus Labs</div>
                <div class="tech-item">Nexus Ventures</div>
                <div class="tech-item">Nexus Academy</div>
                <div class="tech-item">Nexus Blockchain</div>
            </div>
        </div>
    </div>

    <!-- FLUJO DE CAPITAL MULTIDIMENSIONAL -->
    <div class="economic-flow">
        <h3 style="text-align: center; margin-bottom: 1rem;">FLUJO DE CAPITAL MULTIDIMENSIONAL</h3>
        
        <div class="capital-grid">
            <div class="capital-item">
                <h4>💵 CAPITAL FINANCIERO</h4>
                <p>Flujos tradicionales + inversión de impacto</p>
            </div>
            <div class="capital-item">
                <h4>🌿 CAPITAL NATURAL</h4>
                <p>Valor de biodiversidad y servicios ecosistémicos</p>
            </div>
            <div class="capital-item">
                <h4>👥 CAPITAL SOCIAL</h4>
                <p>Valor creado para comunidades y stakeholders</p>
            </div>
            <div class="capital-item">
                <h4>🎯 CAPITAL HUMANO</h4>
                <p>Desarrollo de talento y capacidades</p>
            </div>
        </div>
    </div>

    <!-- FLUJO DE INTERACCIÓN ENTRE ANILLOS -->
    <div class="interaction-flow">
        <h3 style="text-align: center; margin-bottom: 1rem;">FLUJO INTEGRADO: DATOS + OPERACIONES + ECONOMÍA</h3>
        <div style="text-align: center;">
            <strong>8 DOMINIOS → ANILLO 1 → ANILLO 2 → ANILLO 3 → ANILLO 4</strong><br>
            (Base Operacional → Núcleo → Digital → Sostenibilidad → Ecosistema)
        </div>
        <div style="text-align: center; margin-top: 1rem;">
            <strong>FLUJO ECONÓMICO BIDIRECCIONAL</strong><br>
            Cada decisión económica optimiza todos los capitales simultáneamente
        </div>
    </div>
</div>

<div class="footer">
    <p><strong>MIF-NEXUS EVOLUTION FRAMEWORK v2.0 - ARQUITECTURA CON DOMINIO ECONÓMICO</strong></p>
    <p>Sistema Integral para la Transformación Sostenible y Rentable de Operaciones Energéticas</p>
    <p>© 2025 - Fernando Jesús More Torres</p>
</div>

<script>
/* ===== FUNCIÓN PARA POSICIONAR COMPONENTES ===== */
function placeColoredComponents(radius, items, centerX = 600, centerY = 600) {
    items.forEach((obj, i) => {
        const angle = (360 / items.length) * i;
        const rad = angle * Math.PI / 180;

        const x = centerX + radius * Math.cos(rad);
        const y = centerY + radius * Math.sin(rad);

        const el = document.createElement("div");
        el.className = "component";
        el.style.background = obj.color;
        el.innerHTML = obj.text;
        el.dataset.info = obj.info || "";

        el.style.left = (x - 50) + "px";
        el.style.top = (y - 50) + "px";

        // Añadir animación escalonada
        el.style.animationDelay = (i * 0.2) + "s";

        document.querySelector(".canvas").appendChild(el);
        
        // Añadir interactividad
        el.addEventListener('click', function() {
            alert(`Componente: ${obj.text}\n${obj.info || "Información detallada no disponible"}`);
        });
    });
}

/* ===== FUNCIÓN PARA CREAR LÍNEAS DE CONEXIÓN ===== */
function createConnectionLines() {
    const centerX = 600;
    const centerY = 600;
    
    // Crear líneas desde el centro hacia los componentes del anillo 0
    for (let i = 0; i < 8; i++) {
        const angle = (360 / 8) * i;
        const rad = angle * Math.PI / 180;
        
        const endX = centerX + 100 * Math.cos(rad);
        const endY = centerY + 100 * Math.sin(rad);
        
        const line = document.createElement("div");
        line.className = "connection-line";
        
        // Calcular longitud y rotación
        const length = Math.sqrt(Math.pow(endX - centerX, 2) + Math.pow(endY - centerY, 2));
        const rotation = Math.atan2(endY - centerY, endX - centerX) * 180 / Math.PI;
        
        line.style.width = length + "px";
        line.style.left = centerX + "px";
        line.style.top = centerY + "px";
        line.style.transform = `rotate(${rotation}deg)`;
        line.style.animationDelay = (i * 0.3) + "s";
        
        document.querySelector(".canvas").appendChild(line);
    }
}

/* ======= COLORES ======= */
const rojo     = "#e74c3c";
const azul     = "#2980b9";
const verde    = "#27ae60";
const morao    = "#8e44ad";
const naranja  = "#f39c12";
const turquesa = "#16a085";
const rosado   = "#e84393";
const amarillo = "#f1c40f";
const dorado   = "#f39c12";

/* ===== 8 DOMINIOS ===== */
const DOMINIOS = [
    {text:"D1: Recursos", color: rojo, info: "D1: Recursos y Materia Prima - Gestión circular de recursos"},
    {text:"D2: Infraestructura", color: rojo, info: "D2: Infraestructura y Activos - Optimización y resiliencia física"},
    {text:"D3: Datos", color: rojo, info: "D3: Datos, Monitoreo y Control - Decisión basada en datos tiempo real"},
    {text:"D4: Estrategia", color: rojo, info: "D4: Estrategia, Gestión y Gobernanza - Alineación estratégica y sostenibilidad"},
    {text:"D5: Seguridad", color: rojo, info: "D5: Seguridad, Riesgo y Resiliencia - Gestión proactiva de riesgos"},
    {text:"D6: Operaciones", color: rojo, info: "D6: Operaciones y Eficiencia Energética - Optimización operativa y energética"},
    {text:"D7: Transición", color: rojo, info: "D7: Transición Energética Integrada - Gestión de transición hacia sostenibilidad"},
    {text:"💎 D8: Economía", color: dorado, info: "D8: Economía y Finanzas Sostenibles - Rentabilidad integral y flujos regenerativos"}
];

/* ===== COMPONENTES POR ANILLO ===== */

/* ANILLO 1 — Tonos AZULES */
const A1 = [
    {text:"8 Dominios", color: azul, info: "Ocho dominios operativos especializados"},
    {text:"Gestión Integrada", color: azul, info: "Gestión técnica y económica integrada"},
    {text:"Procesos Core", color: azul, info: "Procesos operativos con KPIs financieros"},
    {text:"Optimización", color: azul, info: "Optimización costo-beneficio en tiempo real"},
    {text:"Tiempo Real", color: azul, info: "Ejecución y monitoreo económico en tiempo real"},
    {text:"Predictivos", color: azul, info: "Modelos predictivos económicos avanzados"},
    {text:"Presupuestos", color: azul, info: "Presupuestos dinámicos por dominio"},
    {text:"ROI por Activo", color: azul, info: "Cálculo de ROI por activo y proyecto"}
];

/* ANILLO 2 — Verdes */
const A2 = [
    {text:"Dashboard Nexus", color: verde, info: "Dashboard interactivo con métricas económicas"},
    {text:"API Integración", color: verde, info: "API de integración financiera abierta"},
    {text:"Base Datos", color: verde, info: "Base de datos unificada con datos económicos"},
    {text:"Motor IA Económica", color: verde, info: "Motor de IA y analítica económica avanzada"},
    {text:"Gemelos Digitales", color: verde, info: "Gemelos digitales con simulación económica"},
    {text:"Blockchain", color: verde, info: "Blockchain para transparencia financiera"},
    {text:"S-ROI Calculator", color: verde, info: "Calculadora de ROI Sostenible en tiempo real"},
    {text:"Flujos Multi-capital", color: verde, info: "Seguimiento de flujos multi-capital"}
];

/* ANILLO 3 — Morados / Rosados */
const A3 = [
    {text:"Carbono Negativo", color: morao, info: "Carbono negativo verificado con valor económico"},
    {text:"Agua +", color: morao, info: "Agua neto positivo con ahorros económicos"},
    {text:"Biodiversidad +30%", color: rosado, info: "Biodiversidad incrementada con valor económico"},
    {text:"Economía Circular", color: morao, info: "Economía circular al 95% con ahorros"},
    {text:"Certificaciones", color: rosado, info: "Certificaciones automáticas con primas"},
    {text:"Bonos Verdes", color: morao, info: "Emisión y gestión de bonos verdes"},
    {text:"Mercado Carbono", color: rosado, info: "Participación en mercados de carbono"},
    {text:"Valor de Marca", color: morao, info: "Incremento del valor de marca sostenible"}
];

/* ANILLO 4 — Naranjas */
const A4 = [
    {text:"Comité Nexus", color: naranja, info: "Comité Nexus multi-stakeholder económico"},
    {text:"Innovación Abierta", color: naranja, info: "Innovación abierta con modelos económicos"},
    {text:"Comunidad Dev", color: naranja, info: "Comunidad de desarrollo económico"},
    {text:"Mercados ESG", color: naranja, info: "Acceso a mercados ESG globales"},
    {text:"Educación Económica", color: naranja, info: "Educación continua en finanzas sostenibles"},
    {text:"Nexus Ventures", color: naranja, info: "Nexus Ventures - Fondos de impacto"},
    {text:"Alianzas Estratégicas", color: naranja, info: "Alianzas estratégicas económicas"},
    {text:"Expansión Global", color: naranja, info: "Expansión global con modelos económicos probados"}
];

/* ======= POSICIÓN FINAL ======= */
// 8 Dominios (centro)
placeColoredComponents(100, DOMINIOS);
// Anillos
placeColoredComponents(150, A1);
placeColoredComponents(250, A2);
placeColoredComponents(350, A3);
placeColoredComponents(450, A4);

// Crear líneas de conexión
createConnectionLines();

// Animación de entrada para los anillos
document.addEventListener('DOMContentLoaded', function() {
    const rings = document.querySelectorAll('.ring');
    rings.forEach((ring, index) => {
        setTimeout(() => {
            ring.style.opacity = '1';
        }, index * 300);
    });
    
    // Animación escalonada para las tarjetas
    const cards = document.querySelectorAll('.detail-card');
    cards.forEach((card, index) => {
        setTimeout(() => {
            card.style.animation = `card-enter 0.6s ease-out ${index * 0.1}s both`;
        }, 500);
    });
});
</script>

</body>
</html>
