from django.shortcuts import render
from django.http import HttpResponse
from .models.products import Products
from .models.advertisement import advertisement
from .models.category import Categories
from .models.delivery import Delivery
from django.shortcuts import render, redirect
from django.shortcuts import render, redirect
from django.contrib import messages
from .models.User_Detail import User_Detail
from .models.carts import CartItem
from .models.Main_TABLE import Main_table
from django.contrib.auth.hashers import make_password
from django.contrib import messages

def bill(request):
    return render(request, 'Bill.html')


def payment(request):
     return render(request, 'payment.html')

def chart(request):
     return render(request, 'charts.html')

def datainserted(request):
    profile_name = ''
    if request.method == 'POST':
        name = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password == confirm_password:
            temp_variable = User_Detail(user_name=name, gmail=email, password=password, confirm_password=confirm_password)
            temp_variable.save()
            # Store the profile_name in the session
            request.session['profile_name'] = name
            messages.success(request, 'created account successfully ')
            return render(request, 'carts.html', {'name': name})
        else:
            messages.error(request, "Passwords do not match.")
            return render(request, 'acccountuser.html.html') # Or wherever your signup form is
    return render(request, 'carts.html', {'name': request.session.get('profile_name', '')})


def login_view(request):
    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')
        print(f"Attempted username: {name}")

        authenticated = False
        for user in User_Detail.objects.all():
            if user.user_name == name and user.password == int(password):  # INSECURE!
                authenticated = True
                break

        if authenticated:
            messages.success(request, 'Authenticated sucessfully ')
            request.session['profile_name'] = name
            return render(request,'carts.html',{'name': request.session.get('profile_name', '')})
        else:
            messages.error(request, 'Invalid username or password')
    print(authenticated)
    return render(request, 'loginuser.html')




def first(request):
    return render(request,'first.html')



def login(request):
    return render(request,'loginuser.html')

def delivery(request):
    return render(request,'delivery.html')

def account(request):
    return render(request,'acccountuser.html')

def detail(request):
    return render(request,'Detail_product.html')



def orders(request):
    return render(request,'order.html')

def home(request):
    products = None
    adds = advertisement.getadds()
    cate=Categories.getcategory()

    catid=request.GET.get('category')
    if catid:
        products=Products.getproducts_category(catid)
    else:
        products=Products.getproducts

    context = {
        'items': products,
        'adds': adds,
        'category':cate,
    }
    return render(request, 'home.html', context)
    
def second(request):
    return render(request,'account.html')

def profile(request):
    # Get the username from the session, default to an empty string if not found
    profile_name = request.session.get('profile_name', '')
    user_detail = None # Initialize user_detail to None

    if profile_name: # Only try to fetch if profile_name exists
        try:
            # Attempt to get the User_Detail object based on the username
            user_detail = User_Detail.objects.get(user_name=profile_name)
        except User_Detail.DoesNotExist:
            # Handle the case where the User_Detail is not found (e.g., log, redirect, or display a message)
            print(f"User_Detail for '{profile_name}' not found.")
            # Optionally, clear the session profile_name if it's invalid
            if 'profile_name' in request.session:
                del request.session['profile_name']

    context = {
        'user_detail': user_detail, # Pass the fetched object
        'profile_name': profile_name, # Still pass profile_name for the logout button logic
    }
    return render(request, 'profile.html', context)

def logout_view(request):
    authenticated = False
    print("Logout view called!")
    if 'profile_name' in request.session:
        print(f"Session before deletion: {request.session.items()}")
        del request.session['profile_name']
        print("profile_name deleted from session.")
        print(f"Session after deletion: {request.session.items()}")
        request.session.save()  # Explicitly save the session
    else:
        print("profile_name not found in session.")
    return redirect('second')



def add_cart_backened(request):
    profile_name = request.session.get('profile_name', '')
    print(f"Profile Name from session: {profile_name}")
    user_id = None
    user_detail = User_Detail.objects.get(user_name=profile_name)
    user_id = user_detail.user_id

    if request.method == 'GET':
        item_name = request.GET.get('name')
        price = request.GET.get('price')
        image_url = request.GET.get('image')
        quantity=request.GET.get('quantity')

        if quantity==None:
            quantity=1

        if item_name and price and image_url:
            try:
                price = float(price)  # Convert price to a float
                cart_item = CartItem(userid=user_id,name=item_name, price=price, image=image_url,quantity=quantity )
                cart_item.save()
                print(f"Added '{item_name}' to cart.") # Optional: Logging
            except ValueError:
                print("Invalid price format.") # Optional: Error handling for price
        else:
            print("Missing item details in the request.") # Optional: Logging for missing data

    return render(request, 'carts.html')

#  work here 
def carts(request):
    profile_name = request.session.get('profile_name', '')
    print(f"Profile Name from session: {profile_name}")
    user_id_to_filter = None

    if profile_name:
       
            user_detail = User_Detail.objects.get(user_name=profile_name)
            print(f"User ID from User_Detail for '{profile_name}': {user_detail.user_id}")
            user_id_to_filter = user_detail.user_id
    else:
        user_id_to_filter = 900  # Default user ID if no profile_name in session
    
    cart_items = CartItem.objects.filter(userid=user_id_to_filter)
    
    for item in cart_items:
      item.total_amount = item.price * item.quantity
     
    
    context = {'cart_items': cart_items, 'name': profile_name, 'user_id': user_id_to_filter  }

    return render(request, 'carts.html', context)

# till here 


# order page start 
def add_order_backened(request):
    profile_name = request.session.get('profile_name', '')
    print(f"Profile Name from session: {profile_name}")
    user_id = None

    try:
        # It's better to fetch User_Detail inside a try-except block
        # in case profile_name exists in session but no matching user_detail
        user_detail = User_Detail.objects.get(user_name=profile_name)
        user_id = user_detail.user_id
        print(f"User ID from User_Detail for '{profile_name}': {user_id}")
    except User_Detail.DoesNotExist:
        # Handle the case where the profile_name from session doesn't match a User_Detail
        print(f"User_Detail for '{profile_name}' not found. Cannot add order.")
        # Decide how to handle this:
        # 1. Redirect to an error page or login.
        # 2. Return an error message.
        # 3. Use a default user_id (less secure, but might be desired in some test cases).
        # For now, let's just return a simple error if no user is found.
        return render(request, 'order.html', {'error_message': 'User profile not found.'})
    except Exception as e:
        print(f"An unexpected error occurred while fetching User_Detail: {e}")
        return render(request, 'order.html', {'error_message': 'An internal error occurred.'})

    if request.method == 'GET':
        item_name = request.GET.get('name')
        price_str = request.GET.get('price') # Renamed to price_str as it's initially a string
        quantity_str = request.GET.get('quantity') # Renamed for clarity

        # Default quantity if not provided or invalid
        quantity = 1
        try:
            if quantity_str: # Only try to convert if it's not None or empty
                quantity = int(quantity_str)
        except ValueError:
            print(f"Invalid quantity format received: '{quantity_str}'. Defaulting to 1.")
            # Quantity remains 1 due to initialization

        # Default price if not provided or invalid
        price = 0.0 # Initialize price to a default float value
        if item_name and price_str: # Ensure both are present before trying to convert price
            try:
                price = float(price_str)
            except ValueError:
                print(f"Invalid price format received: '{price_str}'. Cannot add order.")
                return render(request, 'order.html', {'error_message': 'Invalid price format.'})

            # Calculate total_amount. This is exactly what you wanted.
            calculated_total_amount = quantity * price

            try:
                order_item = Main_table(
                    userid=user_id,
                    user_name=profile_name,
                    product_name=item_name,
                    price_per_item=price,
                    quantity=quantity,
                    total_amount=calculated_total_amount # Storing the calculated total
                )
                order_item.save()
                print(f"Successfully added '{item_name}' (Quantity: {quantity}, Price: {price}) to order with total amount: {calculated_total_amount}.")
                # Redirecting after successful POST (or GET in this case) is good practice
                # to prevent re-submission if the user refreshes.
                # Consider using redirect('some_success_url') instead of render('order.html')
                return render(request, 'order.html', {'success_message': f"Order for '{item_name}' added successfully!"})

            except Exception as e:
                print(f"Error saving order item '{item_name}': {e}")
                return render(request, 'order.html', {'error_message': 'Failed to save order item.'})
        else:
            print("Missing item_name or price in the request. Cannot add order.")
            return render(request, 'order.html', {'error_message': 'Missing product details.'})

    # If the request method is not GET, or if processing fails early
    return render(request, 'order.html') # Or redirect, or return an appropriate error.


#  order retreve data from database here 
def orders(request):
    profile_name = request.session.get('profile_name', '')
    print(f"Profile Name from session: {profile_name}")
    user_id_to_filter = None

    if profile_name:
       
            user_detail = User_Detail.objects.get(user_name=profile_name)
            print(f"User ID from User_Detail for '{profile_name}': {user_detail.user_id}")
            user_id_to_filter = user_detail.user_id
    else:
        user_id_to_filter = 900  # Default user ID if no profile_name in session

    order_item = Main_table.objects.filter(userid=user_id_to_filter)
    context = {'order_items': order_item, 'name': profile_name, 'user_id': user_id_to_filter, 'status': "Processing"}
    return render(request, 'order.html', context)
# till here 


def remove_item_cart(request):
    profile_name = request.session.get('profile_name')

    # Basic user login check (minimal)
    if not profile_name:
        messages.error(request, 'Please sign in.')
        return redirect('login_view')

    try:
        # Get user_id assuming User_Detail exists for the profile_name
        user_detail = User_Detail.objects.get(user_name=profile_name)
        user_id = user_detail.user_id

        product_id_to_remove = request.POST.get('item.productid')
        product_id_to_delete = product_id_to_remove
        print(product_id_to_delete)

        deleted_count, _ = CartItem.objects.filter(
            productid=product_id_to_delete,
            userid=user_id
        ).delete()

        if deleted_count > 0:
            messages.success(request, f"All items with Product ID {product_id_to_delete} removed from your cart.")
        else:
            messages.info(request, f"No items with Product ID {product_id_to_delete} found in your cart.")

    except User_Detail.DoesNotExist:
        messages.error(request, 'User profile not found. Please re-login.')
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('carts')


def remove_item_cart(request):
    profile_name = request.session.get('profile_name')

    # Basic user login check (minimal)
    if not profile_name:
        messages.error(request, 'Please sign in.')
        return redirect('login_view')

    try:
        # Get user_id assuming User_Detail exists for the profile_name
        user_detail = User_Detail.objects.get(user_name=profile_name)
        user_id = user_detail.user_id

        product_id_to_remove = request.POST.get('item.productid')
        product_id_to_delete = product_id_to_remove
        print(product_id_to_delete)

        deleted_count, _ = CartItem.objects.filter(
            productid=product_id_to_delete,
            userid=user_id
        ).delete()

        if deleted_count > 0:
            messages.success(request, f"All items with Product ID {product_id_to_delete} removed from your cart.")
        else:
            messages.info(request, f"No items with Product ID {product_id_to_delete} found in your cart.")

    except User_Detail.DoesNotExist:
        messages.error(request, 'User profile not found. Please re-login.')
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('carts')




#  order item deleted 
def cancelled_item_order(request):
    profile_name = request.session.get('profile_name')

    # Basic user login check (minimal)
    if not profile_name:
        messages.error(request, 'Please sign in.')
        return redirect('login_view')

    try:
        # Get user_id assuming User_Detail exists for the profile_name
        user_detail = User_Detail.objects.get(user_name=profile_name)
        user_id = user_detail.user_id

        product_id_to_remove = request.POST.get('item.order_id')
        product_id_to_delete = product_id_to_remove
        print(product_id_to_delete)

        deleted_count, _ = Main_table.objects.filter(
            order_id=product_id_to_delete,
            userid=user_id
        ).delete()

        # if deleted_count > 0:
        #     messages.success(request, f"All items with Product ID {product_id_to_delete} removed from your cart.")
        # else:
        #     messages.info(request, f"No items with Product ID {product_id_to_delete} found in your cart.")

    except User_Detail.DoesNotExist:
        messages.error(request, 'User profile not found. Please re-login.')
    except Exception as e:
        messages.error(request, f"An unexpected error occurred: {e}")

    return redirect('order')


