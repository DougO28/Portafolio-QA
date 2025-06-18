// cypress.config.js
const { defineConfig } = require('cypress');

module.exports = defineConfig({
  e2e: {
    setupNodeEvents(on, config) {
      // Implementa los listeners de eventos de nodo aquí 
    
    },

    // La URL se debe definir aquí
    baseUrl: process.env.CYPRESS_BASE_URL || 'http://localhost:3000',
    specPattern: 'cypress/e2e/**/*.cy.{js,jsx,ts,tsx}',
    supportFile: 'cypress/support/e2e.js',

    // Configuración para el viewport de navegador
    viewportWidth: 1280,
    viewportHeight: 720,
  },
  // Opciones de configuración a nivel de proyecto
  // Se puede añadir más configuraciones aquí (ej. reporter, videos, screenshots)
});