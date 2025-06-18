
describe('Navegación Básica y Verificación de Contenido', () => {
    beforeEach(() => {

        // Utilizar el comando personalizado para visitar la página 
        cy.visitPage('/');
    });

    it('Debe cargar la página principal correctamente', () => {
        // Verifica que el título de la página contenga un texto esperado
        cy.title().should('not.be.empty');
        cy.title().should('contain', 'Tu Aplicación'); // Reemplaza con el título real esperado

        // Verifica que algún elemento clave esté visible en la página
        cy.get('h1').should('be.visible').and('not.be.empty');
    });

    it('Debe navegar a una sección específica si existe', () => {
        // Ejemplo de navegación a otra página (descomenta y adapta)
        // cy.visitPage('/about');
        // cy.url().should('include', '/about');
        // cy.contains('Acerca de nosotros').should('be.visible');
    });

    //  añadir más pruebas aquí
    
});