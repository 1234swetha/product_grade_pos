odoo.define('product_grade_pos.receipt', function (require) {
"use strict";
   var { Orderline } = require('point_of_sale.models');
   var Registries = require('point_of_sale.Registries');
   const CustomOrder = (Orderline) => class CustomOrder extends Orderline {
       export_for_printing() {
       var result = super.export_for_printing(...arguments);
       var product_grade = this.product.grade
       result.product_grade = product_grade
       return result;
   }
   }
       Registries.Model.extend(Orderline, CustomOrder);
   });