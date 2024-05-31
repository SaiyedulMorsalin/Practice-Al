
// const modalContainer = document.getElementById("con-modal");
// const button = document.createElement("div");
// button.innerHTML =`
//         <button   id="modalButton" type="button" class="btn btn-primary">
//             Details 
//         </button>

// `
// modalContainer.appendChild(button);
// document.addEventListener('DOMContentLoaded', function () {
//     var modalButton = document.getElementById('modalButton');
//     var exampleModal = new bootstrap.Modal(document.getElementById('exampleModal'));

//     modalButton.addEventListener('click', function () {
//         exampleModal.show() ;
        
//     });
// });

// const showDetails = (pName)=>{
//     const modalItem = document.getElementById("modalItem");
//     const modal = document.createElement("div");
//     modal.innerHTML = `
//     <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
//     <div class="modal-dialog modal-dialog-centered">
//         <div class="modal-content">
//             <div class="modal-header">
//                 <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
//             </div>
//             <div class="modal-body">
//                 <div class="card">
//                 <img src="..." class="card-img-top" alt="...">
//                 <div class="card-body">
//                     <h5 class="card-title">${pName}</h5>
//                     <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
//                     <a href="#" class="btn btn-primary">Go somewhere</a>
//                 </div>
//                 </div>
//             </div>
            
//         </div>
//         </div>
//         </div>
//     `
//     modalItem.appendChild(modal);
// }
document.addEventListener('DOMContentLoaded', function () {
    var modalButton = document.getElementById('modalButton');
    var modalContainer = document.getElementById('modalContainer');
  
    modalButton.addEventListener('click', function () {
      // Define the modal's HTML content
      var modalContent = `
        <div class="modal fade" id="dynamicModal" tabindex="-1" aria-labelledby="dynamicModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="dynamicModalLabel">Dynamic Modal Title</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                This is the dynamically generated modal content.
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
                <button type="button" class="btn btn-primary">Save changes</button>
              </div>
            </div>
          </div>
        </div>
      `;
  
      // Inject the modal content into the modal container
      modalContainer.innerHTML = modalContent;
  
      // Initialize and show the modal using Bootstrap's JavaScript API
      var dynamicModal = new bootstrap.Modal(document.getElementById('dynamicModal'));
      dynamicModal.show();
    });
  });
  