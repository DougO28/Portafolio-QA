describe ("Test suite - conjunto de pruebas",() => { 

    it("validar Pagina de inicio", () => {
        cy.visit("https://www.demoblaze.com/")
        cy.get(".active > .d-block").should("be.visible")
        cy.get('#cat').contains("CATEGORIES")
    })
    
    it("validar que se puede agregar un producto al carrito", () => {
        cy.visit("https://www.demoblaze.com/")
        cy.get(':nth-child(1) > .card > .card-block > .card-title > .hrefch').click()
        cy.get('.col-sm-12 > .btn').click()
        cy.get('.active > .nav-link').click()
        cy.get(':nth-child(3) > .card > .card-block > .card-title > .hrefch').click()
        cy.get('.col-sm-12 > .btn').click()
        cy.get('.active > .nav-link').click()
        cy.get('#cartur').click()
        cy.get('.col-lg-1 > .btn').click()
        cy.get('#name').type("Douglas")
        cy.get('#country').type("Guatemala")
        cy.get('#city').type("Guatemala")
        cy.get('#card').type("123456789")
        cy.get('#month').type("12")
        cy.get('#year').type("2025")
        cy.get('#orderModal > .modal-dialog > .modal-content > .modal-footer > .btn-primary').click()
        cy.get('.confirm').click()
        
        
    })

    it.only("Prueba de validacion para la actualizacion de graficos", () => {
        cy.visit("https://www.demoblaze.com/")
        cy.get('#login2').click()
        cy.get('#loginusername').type("Douglas")
        cy.get('#loginpassword').type("123456")
        cy.get('#logInModal > .modal-dialog > .modal-content > .modal-footer > .btn-primary').click()
        cy.get('#logInModal > .modal-dialog > .modal-content > .modal-footer > .btn-secondary').click()





    })

})