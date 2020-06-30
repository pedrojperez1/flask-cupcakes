console.log('Lebron is dope');
$(document).ready(populateUL);

async function populateUL(cupcakes) {
    $('#cupcake-list').empty();
    let res = await axios.get('/api/cupcakes');
    for (cupcake of res.data.cupcakes) {
        console.log(cupcake);
        let {flavor, size, rating, image} = cupcake;
        let new_cupcake = newCupcakeCard(flavor, size, rating, image);
        $('#cupcake-list').append(new_cupcake)
    }
}

 let $flavor = $('#flavor')
 let $size = $('#size')
 let $rating = $('#rating')
 let $image = $('#image')

$('#cupcakeForm').submit(function(e) {
    e.preventDefault();
    postNewCupcake($flavor.val(), $size.val(), $rating.val(), $image.val());
    $flavor.val('');
    $size.val('');
    $rating.val('');
    $image.val('');
    populateUL();
});


async function postNewCupcake(flavor, size, rating, image) {
    data = { flavor, size, rating, image };
    console.log(data);
    let res = await axios.post('/api/cupcakes', data);
    console.log(res.status);
}

function newCupcakeCard(flavor, size, rating, image) {
    return `
        <div class="card text-center" style="width: 18rem;">
            <img src="${image}" class="card-img-top" alt="...">
            <div class="card-body">
              <p class="card-text">Flavor: ${flavor}</p>
              <p class="card-text">Size: ${size}</p>
              <p class="card-text">Rating: ${rating}</p>
            </div>
        </div>
    `;
}
