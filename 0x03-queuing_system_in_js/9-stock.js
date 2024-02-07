import express from "express";
const listProducts = [
    {'id': 1, 'name': 'Suitcase 250', 'price': 50, 'stock': 4},
    {'id': 2, 'name': 'Suitcase 450', 'price': 100, 'stock': 10},
    {'id': 3, 'name': 'Suitcase 650', 'price': 350, 'stock': 2},
    {'id': 4, 'name': 'Suitcase 1050', 'price': 550, 'stock': 5}
]


function getItemById(id) {
    return listProducts.find((item) => item.id === id);
}

const app = express();
app.get('/list_products', (req, res) => {
    res.json(listProducts);
});

app.get('/list_products/:itemId', (req, res) => {
    const item = getItemById(parseInt(req.params.itemId));
    if (item) {
        res.json(item);
    } else {
        res.status(404).json({status: 'Product not found'});
    }
});

app.listen(1245);
export default app;
