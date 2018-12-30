# Sales Management
Small django project-sales management system-
The system is designed to be used by traditional stores that at the same time sell online, and need to track there current stock and it's cost.

# Pages
The system has seven main pages
* Add product:
Through this page the seller can add a new product to the system defining its name,type, image and description.
* Add item:
Via this page the seller adds his current stock of a particular product-which was added in add product page- he would select the product type and enter the quantaty and the currancy used to buy that quantaty, total order cost-Total cost including shipping and tax, the system will divide it by quantaty to determing unit cost- finally the user needs to a uniq batch id whic his used to identify this batch of the product.
* Remove item:
Through this page the seller can remove sold items, he needs to select the batch id and the product. Also, he needs to enter the quantaty and the revenue per unit.
* Sales, Products & Batches:
these three pages are used to provide reports to the suer. The min selling price is the break even point for that item, which is the price that a product can be soled for and just return its original cost without any profit. It is calculated based on the fees determined by the seller in the admin page.

* Finally Calculate profit page which is used to calculate the profit the seller just needs to select the type and currancy in addition enter the unit cost and the price in the local market. The system will use the fees defined in the admin page to calculate the min selling price and that differance between it and the price in the local market.