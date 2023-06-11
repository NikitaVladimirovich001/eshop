(function cartHandler() {
$(document).ready(function(){
//    alert($('.product-count')[0].innerHTML);

    $('.btn-delete').click(function (e) {
        e.preventDefault(); // отмена собятия по умолчанию
        let productId = null ;// получаем классы элемента

        e.target.className.split(' ').forEach(function(item) {
            if (item.indexOf('prod') != -1)
                productId = Number(item .split('-')[1]) // получаем id конкретного товара
        });
        console.log(productId);

        $.get(`/cart/delete/${productId}/`,
            success=function (data) {
               if (data.successed) {
                let productsCount = Number($('.product-count')[0].innerHTML);
                let productCount = Number($(`.product-${productId}-count`)[0].innerHTML);
                $(`.${productId}`).remove();
                $('.product-count')[0].innerHTML = productsCount - productCount;
               }
            }
        );
    });

    $('.btn-change').click(function(e) {
        e.preventDefault();

        let productId = null;
        e.target.className.split(' ').forEach(function(item) {
            if(item.indexOf('-change-btn') != -1)
                productId = Number(item.split('-')[1]);
        });

        let oldCount = Number($(`.product-${productId}-count`)[0].innerHTML);
        let count = Number($(`.product-${productId}-change`)[0].value);

        $.get({
            url: `/cart/change/${productId}/${count}/`,
            success: function (data) {
                $(`.product-${productId}-count`)[0].innerHTML = count;
                let absoluteCount = Number($('.product-count')[0].innerHTML);
                absoluteCount -= oldCount -count
                $('.product-count')[0].innerHTML = absoluteCount;
                if (count == 0)
                    $(`.prod-${productId}`).trigger('click');
            },
            error: function (data) {
                alert('Такого товара нет в корзине');
            },
        });
    });
});
})();